import os
import streamlit as st
from langchain_groq import ChatGroq


class GroqLLM:
    def __init__(self,user_controls_input):
        self.user_controls_input = user_controls_input
    
    def get_llm_model(self):
        try:
            groq_api_key = self.user_controls_input["Groq_API_Key"]
            selected_groq_model= self.user_controls_input["selected_model"]
            if groq_api_key=='' and os.environ["Groq_API_Key"]=='':
                st.error("Please enter the groq API key")

            llm = ChatGroq(api_key=groq_api_key, model=selected_groq_model)
        except Exception as e:
            raise ValueError(f"Error occured with the execution: {e}")
        return llm