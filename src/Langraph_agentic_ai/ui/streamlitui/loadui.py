import streamlit as st
import os

from src.Langraph_agentic_ai.ui.uiconfig import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}
        
    def load_ui(self):
        # Set the page configuration with a robot icon
        st.set_page_config(page_title="🤖"+self.config.get_page_title(),layout="wide")

        # Display the title
        st.header("🤖"+self.config.get_page_title())
        st.session_state["IsFetchButtonClicked"] = False
        st.session_state.timeframe=''
        
        with st.sidebar:
            llm_options = self.config.get_llm_options()
            user_case_options = self.config.get_use_case_options()

            self.user_controls["selected_llm"]= st.selectbox("select llm",llm_options)
            
            if self.user_controls["selected_llm"]=='Groq':
                #model options
                model_options = self.config.get_groq_options()
                self.user_controls["selected_model"] = st.selectbox("select model", model_options)
                self.user_controls["Groq_API_Key"] = st.session_state["Groq_API_Key"] = st.text_input("API Key",type="password")

                if not self.user_controls["Groq_API_Key"]:
                    st.warning("Please enter your Groq API Key. Please refer to the documentation here https://groq.com/.")
                    
            ## use case selction

            self.user_controls["selected_usecase"]= st.selectbox("select use case", user_case_options)   
            
            if self.user_controls["selected_usecase"]=='Chatbot with Web' or  self.user_controls["selected_usecase"]=="AI news":   
                os.environ["TAVILY_API_KEY"]=self.user_controls["TAVILY_API_KEY"]=st.session_state["TAVILY_API_KEY"]= st.text_input("TAVILY API Key",type="password")
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("Please enter your TAVILY API Key. Please refer to the documentation here https://tavily.com/.")
            if self.user_controls["selected_usecase"]=="AI news":
                st.subheader(" AI new Explorer")
                
                with st.sidebar:
                    time_frame= st.selectbox(
                        "Select Time Frame",
                        ["Daily","Weekly","Monthly"],   
                        index= 0    
                    )       
                if st.button("Fetch AI News",use_container_width=True):
                    st.session_state.IsFetchButtonClicked = True
                    st.session_state.timeframe = time_frame
                
        return self.user_controls 
            
