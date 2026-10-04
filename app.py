
import streamlit as st

from hr_assistant.pipeline import ask, build_hr_assistant


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="HR Assistant",
    page_icon="✳",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# --------------------------------------------------
# CUSTOM DARK THEME
# --------------------------------------------------

st.markdown("""
<style>

/* App background */
.stApp {
    background: #111111;
    color: #e5e5e5;
}

/* Hide default elements */
header, #MainMenu, footer {
    visibility: hidden;
}

/* Main layout */
.block-container {
    max-width: 780px;
    padding-top: 2.5rem;
    padding-bottom: 5rem;
}

/* Typography */
h1, h2, h3 {
    color: #f5f5f5 !important;
    letter-spacing: -0.8px;
}

p {
    color: #a1a1aa;
    line-height: 1.7;
}

/* Header */
.app-header {
    display: flex;
    align-items: center;
    gap: 12px;
    padding-bottom: 20px;
    border-bottom: 1px solid #262626;
    margin-bottom: 35px;
}

.app-logo {
    width: 38px;
    height: 38px;
    border-radius: 11px;
    background: #24232f;
    color: #c4b5fd;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 21px;
}

.app-name {
    font-size: 16px;
    font-weight: 600;
    color: #f5f5f5;
}

.app-caption {
    font-size: 12px;
    color: #737373;
    margin-top: 3px;
}

/* Welcome */
.welcome {
    padding: 75px 0 35px 0;
}

.welcome h1 {
    font-size: 34px !important;
    font-weight: 600 !important;
    letter-spacing: -1.5px;
    margin-bottom: 12px;
}

.welcome p {
    font-size: 15px;
    color: #888888;
}

/* Suggested questions */
div.stButton > button {
    background: #191919;
    color: #c4c4c4;
    border: 1px solid #303030;
    border-radius: 11px;
    padding: 14px 16px;
    font-size: 13px;
    font-weight: 400;
    text-align: left;
    min-height: 52px;
    transition: all 0.2s ease;
}

div.stButton > button:hover {
    background: #222222;
    border-color: #7770a5;
    color: #e5ddff;
}

/* Chat messages */
[data-testid="stChatMessage"] {
    background: transparent;
    border: none;
    padding: 14px 0;
}

/* Chat input */
[data-testid="stChatInput"] {
    background: transparent;
}

[data-testid="stChatInput"] > div {
    background: #1b1b1b;
    border: 1px solid #353535;
    border-radius: 15px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.15);
}

[data-testid="stChatInput"] textarea {
    color: #eeeeee !important;
    font-size: 14px;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: #737373 !important;
}

/* Chat text */
[data-testid="stChatMessage"] p {
    color: #dedede;
    font-size: 14px;
    line-height: 1.8;
}

/* Chat avatars */
[data-testid="stChatMessageAvatarUser"] {
    background: #292929;
}

[data-testid="stChatMessageAvatarAssistant"] {
    background: #282438;
}

/* Horizontal rule */
hr {
    border-color: #292929;
}

/* Footer */
.footer {
    text-align: center;
    color: #626262;
    font-size: 11px;
    padding-top: 35px;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 6px;
}

::-webkit-scrollbar-thumb {
    background: #393939;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# AGENT
# --------------------------------------------------

@st.cache_resource(show_spinner="Preparing assistant...")
def get_agent():
    return build_hr_assistant()


agent = get_agent()


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("""
<div class="app-header">
    <div class="app-logo">✳</div>
    <div>
        <div class="app-name">People / HR Assistant</div>
        <div class="app-caption">Company policy knowledge base</div>
    </div>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# WELCOME SCREEN
# --------------------------------------------------

selected_question = None

if not st.session_state.messages:

    st.markdown("""
    <div class="welcome">
        <h1>How can I help you?</h1>
        <p>
            Ask anything about company policies, employee benefits,
            leave, or workplace guidelines.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        "<p style='font-size:11px;color:#777;letter-spacing:1px;"
        "font-weight:600;margin-bottom:14px;'>SUGGESTED QUESTIONS</p>",
        unsafe_allow_html=True
    )

    questions = [
        "How many casual leaves can I take?",
        "What is the work from home policy?",
        "Explain the maternity leave policy.",
        "How do I claim reimbursements?"
    ]

    for i, q in enumerate(questions):
        if st.button(q, key=f"q_{i}", use_container_width=True):
            selected_question = q


# --------------------------------------------------
# CHAT HISTORY
# --------------------------------------------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# --------------------------------------------------
# CHAT INPUT
# --------------------------------------------------

question = st.chat_input("Message HR Assistant...")

if selected_question:
    question = selected_question


# --------------------------------------------------
# RESPONSE
# --------------------------------------------------

if question:

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):
            try:
                answer = ask(agent, question)
            except Exception:
                answer = "Something went wrong. Please try again."

        st.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    st.rerun()


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("""
<div class="footer">
    AI-powered · HR Policy Assistant
</div>
""", unsafe_allow_html=True)
