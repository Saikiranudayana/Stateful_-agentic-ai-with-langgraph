from src.Langraph_agentic_ai.state.state import State


class ChatbotWithToolsNode:
    """chatbot with enhanced tools integration"""
    def __init__(self, model):
        self.llm = model
        
    def process(self,state:State)-> dict:
        """process the input state and generate a state reposne with the tools integration"""
        user_input = state["messages"][-1] if state["messages"] else ""
        llm_response = self.llm.invoke([{"role":"user","content":user_input}])


        tool_response= f"Tool integration for :'{user_input}'"
        return {"messages": [llm_response, tool_response]}
    
    def create_chatbot(self,tools):
        """Returns a chbot node fuinction"""
        llm_with_tools = self.llm.bind_tools(tools)
        
        def chatbot_node(state:State):
            """chatbot logic for preprocessing the input state and returning a response"""
            return {"messages":[llm_with_tools.invoke(state["messages"])]}

        return chatbot_node