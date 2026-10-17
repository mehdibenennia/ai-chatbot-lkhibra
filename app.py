
import json
import os

import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Lkhibra AI Chatbot",
    page_icon="🤖"
)

st.title("Lkhibra AI Chatbot")
st.caption("Ask me anything about Lkhibra Academy.")

# Load chatbot knowledge
with open("knowledge.json", "r", encoding="utf-8") as file:
    knowledge = json.load(file)

# Initialize Groq client
api_key = os.getenv("GROQ_API_KEY")

if not api_key or api_key == "your_groq_api_key_here":
    st.error("Please configure GROQ_API_KEY in your .env file.")
    st.stop()

client = Groq(api_key=api_key)

# Create system instructions from JSON
system_prompt = f"""
Personality:
{knowledge["personality"]}

Instructions:
{knowledge["instructions"]}

Knowledge:
{json.dumps(knowledge["academy"], ensure_ascii=False)}
"""

# Initialize conversation memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Clear conversation button
if st.button("Clear conversation"):
    st.session_state.messages = []
    st.rerun()

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input("Type your message...")

if prompt:
    # Save and display user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant"):
        try:
            with st.spinner("Thinking..."):
                response = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[
                        {
                            "role": "system",
                            "content": system_prompt
                        },
                        *st.session_state.messages
                    ],
                    temperature=0.3
                )

                answer = response.choices[0].message.content

            st.markdown(answer)

            # Save assistant response
            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

        except Exception as error:
            st.error(f"API error: {error}")
