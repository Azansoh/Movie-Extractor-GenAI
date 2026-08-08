import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# Load environment variables
load_dotenv(override=True)

# --------------------------------------------------
# STREAMLIT PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Mistral AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Azan First AI Chatbot")
st.caption("A simple AI assistant that can chat with you in different personalities. Powered by Mistral AI.")

# --------------------------------------------------
# 1. INITIALIZE SESSION STATE
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------
# 2. SIDEBAR CONFIGURATION
# --------------------------------------------------
st.sidebar.header("⚙️ Settings")

mode = st.sidebar.selectbox(
    "Choose AI Personality",
    ["Funny AI", "Angry AI", "Sad AI"]
)

system_prompts = {
    "Funny AI": "You are a funny AI assistant.",
    "Angry AI": "You are an angry AI assistant.",
    "Sad AI": "You are a sad AI assistant."
}

# --------------------------------------------------
# 3. UPDATE SYSTEM MESSAGE (Without deleting history)
# --------------------------------------------------
current_system_prompt = SystemMessage(content=system_prompts[mode])

if len(st.session_state.messages) == 0:
    st.session_state.messages.append(current_system_prompt)
else:
    # Update system message at index 0 without clearing other messages
    st.session_state.messages[0] = current_system_prompt

# Manual button to reset chat when YOU want
if st.sidebar.button("🗑️ Clear Chat History", use_container_width=True):
    st.session_state.messages = [current_system_prompt]
    st.rerun()

# --------------------------------------------------
# 4. DISPLAY CHAT HISTORY
# --------------------------------------------------
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# --------------------------------------------------
# 5. MODEL INITIALIZATION
# --------------------------------------------------
model = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0.7
)

# --------------------------------------------------
# 6. CHAT INPUT & HANDLING
# --------------------------------------------------
user_input = st.chat_input("Type your message...")

if user_input:
    # Render user input in UI
    with st.chat_message("user"):
        st.write(user_input)

    # Append user message to history
    st.session_state.messages.append(HumanMessage(content=user_input))

    # Invoke model with the entire history
    response = model.invoke(st.session_state.messages)

    # Append & render AI message
    st.session_state.messages.append(AIMessage(content=response.content))
    with st.chat_message("assistant"):
        st.write(response.content)