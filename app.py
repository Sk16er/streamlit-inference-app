import streamlit as st
from transformers import pipeline

# Set the page configuration for dark mode
st.set_page_config(page_title="AI Assistant", page_icon="🤖", layout="centered")

# Title and intro
st.title("AI Assistant 🤖")
st.markdown("""
    ## Welcome to your Personal Assistant!
    Ask me anything, and I’ll do my best to assist you. The AI is powered by `meta-llama/Llama-3.1-8B-Instruct`.
    - **Sidebar**: Start a new conversation or adjust settings.
    - **Dark Mode**: I've made sure to give you a cool, modern interface to keep things sleek and smooth!
""")

# Load the LLM model (meta-llama/Llama-3.1-8B-Instruct)
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="meta-llama/Llama-3.1-8B-Instruct")

# Sidebar: To start a new conversation
st.sidebar.title("Start New Conversation")
if st.sidebar.button("Clear Conversation"):
    st.session_state['messages'] = []

# Initialize conversation history if not already in session_state
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# User Input Textbox
user_input = st.text_input("You: ", "")

# Handle interaction when the user submits a question
if user_input:
    # Add user question to the conversation history
    st.session_state['messages'].append({"role": "user", "content": user_input})

    # Generate AI response using the Llama model
    model = load_model()
    response = model(f"Question: {user_input} Answer: ")

    # Extract the generated text (AI response)
    answer = response[0]['generated_text']

    # Add AI response to conversation history
    st.session_state['messages'].append({"role": "assistant", "content": answer})

# Display the conversation history (questions and answers)
for message in st.session_state['messages']:
    if message["role"] == "user":
        st.markdown(f"<div class='user-message'>{message['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='assistant-message'>{message['content']}</div>", unsafe_allow_html=True)

# Custom CSS to style the chatbot interface (dark mode)
st.markdown("""
    <style>
        body {
            background-color: #333;
            color: white;
        }
        .user-message {
            background-color: #4CAF50;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
            text-align: right;
        }
        .assistant-message {
            background-color: #2F4F4F;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
            text-align: left;
        }
        .stTextInput>div>div>input {
            background-color: #444;
            color: white;
            border-radius: 15px;
            padding: 10px;
            font-size: 18px;
        }
        .stTextInput>div>div>input:focus {
            background-color: #555;
        }
        .stSidebar {
            background-color: #222;
            color: white;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

