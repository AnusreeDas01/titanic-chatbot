import sys
import os
import streamlit as st

# ✅ Ensure Python can find the `backend` directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.query_agent import process_query_with_llm  # ✅ Now it should work

st.set_page_config(page_title="Titanic Chatbot", page_icon="🚢", layout="wide")

st.title("🚢 Titanic Chatbot")
st.write("Ask me anything about Titanic passengers!")

query = st.text_input("Enter your question:")

if st.button("Ask"):
    with st.spinner("Thinking..."):
        response = process_query_with_llm(query)

        # ✅ Check if response is a Matplotlib figure
        if isinstance(response, object) and hasattr(response, "get_figure"):
            st.pyplot(response)  # ✅ Display histogram
        else:
            st.write(response)  # ✅ Show text response
