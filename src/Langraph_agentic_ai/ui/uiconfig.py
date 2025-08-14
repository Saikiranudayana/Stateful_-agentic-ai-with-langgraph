from configparser import ConfigParser


class Config:
    def __init__(self, config_file=r"C:\Users\saiki\OneDrive\Desktop\Stateful agentic ai wiht langgraph\src\Langraph_agentic_ai\ui\uiconfig.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(",")
    def get_use_case_options(self):
        return self.config["DEFAULT"].get("USE_CASE_OPTIONS").split(",")
    def get_groq_options(self):
        return self.config["DEFAULT"].get("GROQ_OPTIONS").split(",")
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")
    
    
