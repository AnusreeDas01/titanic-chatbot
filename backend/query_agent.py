import os
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()

# ✅ Load Titanic dataset (modify path if needed)
DATA_PATH = os.path.join(os.path.dirname(__file__), "../data/titanic.csv")
df = pd.read_csv(DATA_PATH)

# ✅ Get Together AI API Key
api_key = os.getenv("TOGETHER_AI_API_KEY")

if not api_key:
    raise ValueError("❌ API Key not found. Set TOGETHER_AI_API_KEY in .env.")

# ✅ Use a Free Together AI Model
llm = ChatOpenAI(
    model="meta-llama/Llama-3-8b-chat-hf",  # ✅ Free serverless model
    temperature=0.2,
    openai_api_key=api_key,
    base_url="https://api.together.xyz/v1",
)

def process_query_with_llm(question):
    """Process queries using LangChain & Together AI, with histogram support."""
    
    # ✅ Detect if user asks for a histogram
    if "histogram" in question.lower() and "age" in question.lower():
        return generate_histogram()

    system_prompt = "You are an AI chatbot analyzing the Titanic dataset. Answer accurately."

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=question),
    ]

    response = llm.invoke(messages)  
    return response.content  # ✅ Extract the response correctly

def generate_histogram():
    """Generate a histogram of passenger ages and return it as a Streamlit figure."""
    
    fig, ax = plt.subplots()
    ax.hist(df["Age"].dropna(), bins=20, edgecolor="black")
    ax.set_title("Histogram of Passenger Ages")
    ax.set_xlabel("Age")
    ax.set_ylabel("Frequency")

    return fig  # ✅ Return the figure to Streamlit
