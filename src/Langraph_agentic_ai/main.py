import streamlit as st
from src.Langraph_agentic_ai.ui.streamlitui.loadui import LoadStreamlitUI
from src.Langraph_agentic_ai.llms.groqllm import GroqLLM
from src.Langraph_agentic_ai.graphs.graph_builder import GraphBuilder
from src.Langraph_agentic_ai.ui.streamlitui.display_result import DisplayResultStreamlit

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
        st.error("Error: failed to load the input from the ui")
        return
    if st.session_state.IsFetchButtonClicked:
        user_message= st.session_state.timeframe
    else:
        user_message= st.chat_input("Enter your message: ")

    if user_message:
        try:
            obj_llm_config = GroqLLM(user_controls_input=user_controls)
            model = obj_llm_config.get_llm_model()
            
            if not model:
                st.error("Error: failed to load the language model.")
                return
            
            usecase = user_controls.get('selected_usecase')
            if not usecase:
                st.error("Error: failed to get the selected use case.")
                return
            
            ## graph builder
            graph_builder = GraphBuilder(model)
            try :
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: {e}")
                return
            
            
        except Exception as e:
            st.error(f"Error: {e}")
            return