import streamlit as st
from chatbot import get_movie_recommendations, generate_response

st.set_page_config(page_title="CineMate 🎬", page_icon="🎬")

st.title("🎬 CineMate - AI Movie Companion")
st.write("Chat with CineMate about movie recommendations, trivia, theories, and more!")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "content": "You are CineMate, an AI movie expert who helps users with smart, thoughtful film recommendations, trivia, and fan theories."}
    ]

# Chat input box
user_input = st.chat_input("Ask me anything about movies...")

if user_input:
    # Append user's message to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Get assistant reply
    reply = generate_response(st.session_state.chat_history)

    # Append assistant's reply to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": reply})

# Display conversation
for msg in st.session_state.chat_history[1:]:  # Skip system prompt
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    elif msg["role"] == "assistant":
        st.chat_message("assistant").write(msg["content"])
