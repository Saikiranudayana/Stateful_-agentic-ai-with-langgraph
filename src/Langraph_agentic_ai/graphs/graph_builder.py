from langgraph.graph import StateGraph,START,END
from src.Langraph_agentic_ai.state.state import State
from src.Langraph_agentic_ai.Nodes.basicchatbot_node import BasicChatbotNode


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
        self.graph_builder.add_node("ChatbotNode", self.basic_chatbot_node.p)
        self.graph_builder.add_edge(START, "ChatbotNode")
        self.graph_builder.add_edge("ChatbotNode", END)
        
        
    def setup_graph(self,usecase:str):
        """sets the graph bsed on the use case"""

        if usecase=="BasicChatbot":
            self.basic_chatbot_build_graph()