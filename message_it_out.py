from google import genai
from google.genai import types
import streamlit as st
import messageit


x=""

def generate(user, message, emotion):
    client = genai.Client(
        api_key="",
    )

    model = "gemini-2.0-flash-lite"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=f"""I have a message from {user}. message : {message}. give me a proper reply to it. My emotion about this message is {emotion}.
"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""only give me the reply nothing else.
"""),
        ],
    )

    full_response = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        full_response += chunk.text 
    return full_response 

if __name__ == "__main__":
    st.markdown("""
    <style>
    body {
        background-color: #343541;
        color: white;
    }
    .main {
        background-color: #343541;
    }
    div[data-testid="stTextArea"] textarea {
        background-color: #40414f;
        color: white;
        font-size: 1rem;
        border-radius: 8px;
        padding: 10px;
    }
    div[data-baseweb="select"] {
        background-color: #40414f;
        color: white;
    }
    div[data-testid="stSelectbox"] label {
        color: #ddd;
    }
    button[kind="primary"] {
        background-color: #10a37f;
        color: white;
        font-weight: bold;
        border-radius: 8px;
    }
    .chat-box {
        border-radius: 10px;
        padding: 20px;
        background-color: #40414f;
        margin-top: 10px;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("Message it Out")

    user_message = st.text_area("✉️ Enter your message:", placeholder="Type your message here...", height=150)

    emotion = st.selectbox(
        "😄 How should the message be interpreted (Emotion)?",
        ["Happy", "Sad", "Angry", "Neutral", "Excited", "Sarcastic", "Grateful"]
    )

    relation = st.selectbox(
        "👤 Relationship with the recipient:",
        ["Friend", "Family", "Colleague", "Stranger", "Partner", "Teacher", "Boss"]
    )

    if st.button("🚀 Submit"):
        x = generate(relation, user_message, emotion)
        st.spinner("Generating message...") 
        st.text(f"Generated Message: {x}")
        messageit.send_message(x, "+919875090935")
           
          
          