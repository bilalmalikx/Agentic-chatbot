import os
import streamlit as st
from langchain_openai import ChatOpenAI

class OpenAILLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            # API key from user input or environment
            openai_api_key = self.user_controls_input.get("OPENAI_API_KEY", "") or os.environ.get("OPENAI_API_KEY", "")
            selected_openai_model = self.user_controls_input["selected_openai_model"]

            if not openai_api_key:
                st.error("⚠️ Please enter the OpenAI API KEY")
                return None

            # Initialize LLM
            llm = ChatOpenAI(
                api_key=openai_api_key,
                model=selected_openai_model,
                temperature=0.7
            )

        except Exception as e:
            raise ValueError(f"Error occurred with exception: {e}")
        return llm
