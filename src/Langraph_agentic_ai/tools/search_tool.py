from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    """
       List out all the tools which are used in the chatbot.
    """
    tools= [TavilySearchResults(max_results=2)]
    return tools

def create_tool_node(tools):
    """creates and return a tool node for the graph"""
    return ToolNode(tools=tools)
