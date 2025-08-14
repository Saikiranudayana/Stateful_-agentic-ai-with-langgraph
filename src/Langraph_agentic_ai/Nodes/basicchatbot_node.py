from src.Langraph_agentic_ai.state.state import State

class BasicChatbotNode:
    """
    A basic chatbot node for handling user input and generating responses.
    """
    def __init__(self,model):
        self.llm = model
        
    def process(self,state:State)->dict:
        """
        process the input sate and generate the chatbot response
        """
        return {"messages":self.llm.invoke(state['messages'])}
        
           
        
        