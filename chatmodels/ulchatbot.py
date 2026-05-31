from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.9
)

st.title("🤖 AI Chatbot")

# Mode Selection
choice = st.selectbox(
    "🎭 Choose your AI mode",
    ["😂 Funny", "😡 Angry", "😢 Sad"]
)

if choice == "😡 Angry":
    mode = "You are an angry AI agent. You respond aggressively and impatiently."

elif choice == "😂 Funny":
    mode = "You are a funny AI agent. You respond with humor and jokes."

else:
    mode = "You are a sad AI agent. You respond with sadness and empathy."

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=mode)
    ]

# Display chat history
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write("🧑 " + message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write("🤖 " + message.content)

# User input
prompt = st.chat_input("💬 Type your message here...")

if prompt:
    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    with st.chat_message("user"):
        st.write("🧑 " + prompt)

    response = model.invoke(st.session_state.messages)

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

    with st.chat_message("assistant"):
        st.write("🤖 " + response.content)