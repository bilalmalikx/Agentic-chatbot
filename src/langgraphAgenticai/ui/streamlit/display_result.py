import streamlit as st

class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        """
        Display chat messages (User + Assistant) on Streamlit UI
        without extra background styling.
        """
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message

        if usecase == "Basic Chatbot":
            with st.container():
                # Stream through graph responses
                for event in graph.stream({'messages': ("user", user_message)}):
                    for value in event.values():
                        
                        # 🧑 User message
                        with st.chat_message("user", avatar="🧑"):
                            st.write(user_message)

                        # 🤖 Assistant message
                        with st.chat_message("assistant", avatar="🤖"):
                            st.write(value['messages'].content)
