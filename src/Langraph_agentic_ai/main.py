import streamlit as st
from src.Langraph_agentic_ai.ui.streamlitui.loadui import LoadStreamlitUI

def load_langraph_agentic_ai_app():
    """
    Load the Langraph Agentic AI application using Streamlit UI.
    This function initializes the Streamlit UI components and displays the application.
    sets up the user interface for interacting with the Langraph Agentic AI model.
    implements the necessary callbacks and logic for user interactions.
    """
    
    ## load ui
    ui = LoadStreamlitUI()
    user_controls = ui.load_ui()
    if not user_controls:
        st.error("Erro : failed ot load the input from the ui")
        return
    
    user_message= st.chat_input("Enter your message: ")
    
    # if user_message:
        # try:
            # obj_llm_config = GroqLLM(user_controls_input=user_controls)
            # model = obj_llm_config.get_llm_model()
            # 
            # if not model:
                # st.error("Error: failed to load the language model.")
                # return
            # 
            # usecase = user_controls.get('selected_usecase')
            # if not usecase:
                # st.error("Error: failed to get the selected use case.")
                # return 
