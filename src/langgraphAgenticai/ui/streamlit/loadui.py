import streamlit as st
from src.langgraphAgenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title="🤖 " + self.config.get_page_title(), layout="wide")
        st.header("🤖 " + self.config.get_page_title())

        with st.sidebar:
            # Get options from config
            llm_options = self.config.get_llm_option()
            usecase_options = self.config.get_usecase_options()

            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"].strip() == "OpenAI":
                # Model selection
                model_options = self.config.get_openai_option()
                self.user_controls["selected_openai_model"] = st.selectbox("Select Model", model_options)
                
                # API Key
                self.user_controls["OPENAI_API_KEY"] = st.session_state["OPENAI_API_KEY"] = st.text_input(
                    "API Key", type="password"
                )

                # Validate API key
                if not self.user_controls["OPENAI_API_KEY"]:
                    st.warning("⚠️ Please enter your OpenAI API key. Get one at: https://platform.openai.com/account/api-keys")
            
            # Usecase selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecases", usecase_options)

        return self.user_controls
