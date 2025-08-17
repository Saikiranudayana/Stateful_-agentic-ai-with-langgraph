from tavily import TavilyClient
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage
import os

class AINewsNode:
    def __init__(self,llm):
        """ Initialize the AINewsNode with a language model """
        self.tavily = TavilyClient()
        self.llm= llm
        
        ## this is used to capture the various text so that they can be used later steps
        
        self.state={}
        
        
    def fetch_news(self,state:dict)-> dict:
        """ Fetch ai news based on the specified frequency
        Args:
            state (dict): The state dictionary containing relevant information.
        Returns:
            dict: A dictionary containing the fetched news articles.
        """  
        # Support multiple input shapes: plain string, list of messages, or objects with .content
        raw = state.get('messages')
        if isinstance(raw, str):
            freq_in = raw.strip().lower()
        elif isinstance(raw, (list, tuple)) and raw:
            first = raw[0]
            freq_in = (getattr(first, 'content', first) or "").strip().lower()
        else:
            freq_in = str(raw or "daily").strip().lower()

        # Normalize common variants
        if freq_in in ("d", "day", "daily"):
            frequency = "daily"
        elif freq_in in ("w", "week", "weekly"):
            frequency = "weekly"
        elif freq_in in ("m", "month", "monthly"):
            frequency = "monthly"
        else:
            frequency = "daily"

        self.state['frequency'] = frequency
        time_range_map = {'daily': 'd', 'weekly': 'w', 'monthly': 'm'}
        days_map = {'daily': 1, 'weekly': 7, 'monthly': 30}
        
        response= self.tavily.search(
            query= "Artificial intelligence news across the globe or in India",
            topic="news",
            time_range= time_range_map[frequency],
            include_answer = "advanced",
            max_results= 20,
            days = days_map[frequency]
        )
        
        state['new_data']= response.get('results',[])
        self.state['new_data'] = state['new_data']
        return state

    def summarize_news(self, state: dict) -> dict:
        """Summarize fetched news into clean Markdown using the LLM and return messages.

        Returns a graph-friendly state: {"messages": [AIMessage]}.
        """
        news_items = self.state.get("new_data", [])
        if not news_items:
            msg = AIMessage(content="No news items available to summarize.")
            self.state["summary"] = msg.content
            return {"messages": [msg]}

        # Build a compact string for the model
        article_str = "\n\n".join(
            [
                "\n".join(
                    filter(
                        None,
                        [
                            f"Title: {item.get('title', '')}" if item.get("title") else "",
                            f"Date: {item.get('date', '')}" if item.get("date") else "",
                            f"Source: {item.get('source', '')}" if item.get("source") else "",
                            f"URL: {item.get('url', '')}" if item.get("url") else "",
                            f"Content: {item.get('content', '')}" if item.get("content") else "",
                        ],
                    )
                )
                for item in news_items
            ]
        )

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    (
                        """
                        Summarize the AI news articles into Markdown. For each item include:
                        - Date
                        - Title
                        - 2–3 concise bullet points capturing the latest info
                        - Source
                        - Link
                        If a field is missing, omit it gracefully. Keep it readable.
                        """
                    ).strip(),
                ),
                ("user", "Summarize the following news articles in Markdown:\n{news_items}"),
            ]
        )

        chain = prompt | self.llm
        result = chain.invoke({"news_items": article_str})
        if isinstance(result, AIMessage):
            message = result
        else:
            content = getattr(result, "content", None) or str(result)
            message = AIMessage(content=content)

        self.state["summary"] = message.content
        return {"messages": [message]}
    
    def save_results(self,state):
        frequency = self.state.get('frequency', 'daily').lower()
        summary = self.state.get('summary', '')
        out_dir = os.path.join(".", "AINews")
        os.makedirs(out_dir, exist_ok=True)
        # Align with UI expectation: ./AINews/{frequency}_summary.md
        filename = os.path.join(out_dir, f"{frequency}_summary.md")
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"# {frequency.capitalize()} AI News Summary\n\n")
            file.write(summary)
        self.state['filename'] = filename
        return self.state
