import streamlit as st
from langchain_core.messages import HumanMessage,AIMessage,ToolMessage
import json


class DisplayResultStreamlit:
    def __init__(self,usecase,graph,user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message
        
    def display_result_on_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message

        if usecase.strip().lower() == "basic chatbot":
            for event in graph.stream({"messages": ("user", user_message)}):
                print(event.values())
                for value in event.values():
                    print(value['messages'])
                    with st.chat_message("user"):
                        st.write(user_message)
                    with st.chat_message("assistant"):
                        st.write(value['messages'].content)
                        
        elif usecase.strip().lower() == "chatbot with web":
            initial_state = {"messages": [user_message]}
            try:
                res = graph.invoke(initial_state)
                # Debug output for the full result
                st.info(f"Raw result: {res}")
                if not res or "messages" not in res:
                    st.error("No messages returned from the graph. Check graph logic and node outputs.")
                    return
                for message in res["messages"]:
                    if type(message) == HumanMessage:
                        with st.chat_message("user"):
                            st.write(user_message)
                    elif type(message) == ToolMessage:
                        with st.chat_message("tool"):
                            st.write("Tool call started")
                            st.write(message.content)
                            st.write("Tool call ended")
                    elif type(message) == AIMessage:
                        with st.chat_message("assistant"):
                            st.write(message.content)
                    else:
                        st.warning(f"Unknown message type: {type(message)}. Message: {message}")
            except Exception as e:
                st.error(f"Exception during graph invocation: {e}")
                import traceback
                st.text(traceback.format_exc())


