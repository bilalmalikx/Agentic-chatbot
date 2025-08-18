from configparser import ConfigParser

class Config:
    def __init__(self, config_file="./src/langgraphAgenticai/ui/uiconfigfile.ini"):
        self.config_file = ConfigParser()
        self.config_file.read(config_file)
          
    def get_llm_option(self):
        return self.config_file["DEFAULT"].get("LLM_OPTIONS").split(",")
    
    def get_usecase_options(self):
        return self.config_file["DEFAULT"].get("USECASE_OPTIONS").split(",")
    
    def get_openai_option(self):
        return self.config_file["DEFAULT"].get("OPENAI_MODEL_OPTIONS").split(",")
    
    def get_page_title(self):
        return self.config_file["DEFAULT"].get("PAGE_TITLE")
