import groq
import streamlit as st


def get_response(prompt, temperature, max_tokens, persona):
    client = groq.Client(api_key="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")  # Replace with your Groq API Key
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": f"You are a {persona} chatbot."},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content.strip()

# Streamlit UI
st.title("😈 Sassy Chatbot")
st.sidebar.header("Settings")

# Customization options
temperature = st.sidebar.slider("Creativity (Temperature)", 0.0, 1.0, 0.7)
max_tokens = st.sidebar.slider("Max Response Length", 50, 4000, 200)
persona = st.sidebar.selectbox("Chatbot Persona", ["friendly", "sarcastic", "formal", "humorous"])

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.chat_input("Type your message...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    
    # Get chatbot response
    bot_response = get_response(user_input, temperature, max_tokens, persona)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.write(bot_response)