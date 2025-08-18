import streamlit as st
from src.langgraphAgenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        # Page setup
        st.set_page_config(
            page_title="🤖 " + self.config.get_page_title(),
            layout="wide",
            initial_sidebar_state="expanded"
        )

        # Custom header with style
        st.markdown(
            f"""
            <div style="text-align:center; padding: 10px; background-color:#2C3E50; border-radius:10px;">
                <h1 style="color:white;">🤖 {self.config.get_page_title()}</h1>
                <p style="color:#BDC3C7;">An interactive AI assistant powered by LangGraph + OpenAI</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Sidebar
        with st.sidebar:
            st.markdown("### ⚙️ Settings")

            # Get options from config
            llm_options = self.config.get_llm_option()
            usecase_options = self.config.get_usecase_options()

            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox("🔍 Select LLM", llm_options)

            if self.user_controls["selected_llm"].strip() == "OpenAI":
                # Model selection
                model_options = self.config.get_openai_option()
                self.user_controls["selected_openai_model"] = st.selectbox("🤖 Select Model", model_options)
                
                # API Key
                self.user_controls["OPENAI_API_KEY"] = st.session_state["OPENAI_API_KEY"] = st.text_input(
                    "🔑 Enter API Key", type="password", placeholder="sk-..."
                )

                # Validate API key
                if not self.user_controls["OPENAI_API_KEY"]:
                    st.warning("⚠️ Please enter your OpenAI API key. Get one at: https://platform.openai.com/account/api-keys")
            
            # Usecase selection
            self.user_controls["selected_usecase"] = st.selectbox("📌 Select Usecase", usecase_options)

        return self.user_controls
