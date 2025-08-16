from langgraph.graph import StateGraph,START,END
from src.Langraph_agentic_ai.state.state import State
from src.Langraph_agentic_ai.Nodes.basicchatbot_node import BasicChatbotNode
from src.Langraph_agentic_ai.tools.search_tool import get_tools, create_tool_node
from langgraph.prebuilt import ToolNode,tools_condition

class GraphBuilder():
    def __init__(self,model):
        self.llm= model
        self.graph_builder=StateGraph(State)
        
    def basic_chatbot_build_graph(self):
        """
        This a basic chatbot graph using langgraph.
        THis method is implemented to using the node 'Basicchatbot node' class
        and integrate it with the overall graph.the caht bot node is set both the entry and exit pointt
        """
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("ChatbotNode", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "ChatbotNode")
        self.graph_builder.add_edge("ChatbotNode", END)

    def chatbot_with_tools_build_graph(self):
        """
        This method builds a chatbot graph with web browsing capabilities.
        An advanced chatbot node is created with web browsing capabilities.
        with chatbot and a tool node for the integration web browsing.
        
        """
        ## define tools and toolnode
        tools = get_tools()
        tool_node = create_tool_node(tools)
        
        ## define the llm
        llm= self.llm
        
        ## define the chatbot node
        
        
        ## add nodes
        self.graph_builder.add_node("Chatbot","")
        self.graph_builder.add_node("ToolNode", tool_node)
        
        self.graph_builder.add_edge(START, "Chatbot")
        self.graph_builder.add_conditional_edges("Chatbot",tools_condition)
        self.graph_builder.add_edge("ToolNode", "Chatbot")
        self.graph_builder.add_edge("Chatbot", END)

    def setup_graph(self, usecase: str):
        """sets the graph based on the use case"""
        if usecase.strip().lower() == "basic chatbot":
            self.basic_chatbot_build_graph()
        if usecase.strip().lower() == "Chatbot with Web":
            self.chatbot_with_tools_build_graph()
        return self.graph_builder.compile()

            
if __name__ == "__main__":
    import sys
    from src.Langraph_agentic_ai.llms.groqllm import GroqLLM
    # Example user_controls_input, replace with actual input as needed
    user_controls_input = {
        "Groq_API_Key": "YOUR_GROQ_API_KEY",
        "selected_model": "qwen/qwen3-32b"
    }
    model = GroqLLM(user_controls_input).get_llm_model()
    graph_builder = GraphBuilder(model)
    graph_builder.setup_graph("BasicChatbot")
    print("Graph has been built successfully.")
