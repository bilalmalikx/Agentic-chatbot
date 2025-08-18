import streamlit as st
from src.langgraphAgenticai.ui.streamlit.loadui import LoadStreamlitUI

def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while 
    implementing exception handling for robustness.
    """
    # Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return
    
    # Chat input box
    user_message = st.chat_input("Enter your message:")
    if user_message:
        st.write(f"User: {user_message}")
        # yahan tum apna LLM response logic likh sakte ho
