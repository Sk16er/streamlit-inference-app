import streamlit as st
from transformers import pipeline

# Set page config for a nice layout
st.set_page_config(page_title="Inference Provider", page_icon="🤖", layout="wide")

# Title and description
st.title("Inference Provider")
st.markdown("""
    This app uses the deepset/roberta-base-squad2 model to provide question-answering capabilities.
    You can ask a question, and the model will attempt to provide an answer based on the context.
    Sign in with your Hugging Face account to use this feature.
""")

# Sidebar for login information
st.sidebar.markdown("### Login with Hugging Face")
st.sidebar.markdown("Sign in to use the Hugging Face API and access model inference.")

# Add a text input for the question and a button to trigger the answer
question = st.text_input("Ask a question:", "")
answer = None

# Load the Hugging Face model for question answering
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

# Function to handle question answering
if question:
    answer = qa_pipeline({
        'context': "Hugging Face is creating a tool that democratizes AI. The deepset/roberta-base-squad2 model is great for answering questions from a given context.",
        'question': question
    })

    # Display the answer in a nice format
    st.markdown(f"**Answer:** {answer['answer']}")

# Add styling (to make the UI look more like a chat)
st.markdown("""
    <style>
        .stTextInput>div>div>input {
            border-radius: 10px;
            padding: 15px;
            font-size: 16px;
        }
        .stMarkdown {
            padding: 20px;
            background-color: #f5f5f5;
            border-radius: 10px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)
