import streamlit as st

import chatter

chat = chatter.Chatter()

st.title("✉️ emailGPT")
st.subheader("a quick and easy interface to generate emails with ChatGPT")


sender = st.text_input(label="Sender's Name", value="")
recipient = st.text_input(label="Recipient's Name", value="")
subject = st.text_input(label="Subject Line", value="")
topic = st.text_input(label="Topic", value="")

tone = st.radio("Tone", ("excited", "happy", "neutral", "sad", "angry"), index=2)

generate_email = st.button("Generate Email")

if generate_email:
    job = {
        "sender": sender,
        "recipient": recipient,
        "subject": subject,
        "topic": topic,
        "tone": tone,
    }
    message = chat.email_from_job(job=job)
    st.write(message)


with st.sidebar:
    st.markdown(
        "[About ChatGPT](https://openai.com/blog/chatgpt/)", unsafe_allow_html=True
    )
    st.markdown(
        "[This app on GitHub](https://github.com/lucasmccabe/emailGPT)",
        unsafe_allow_html=True,
    )
    st.markdown(
        "[Lucas H. McCabe](https://lucasmccabe.github.io/)", unsafe_allow_html=True
    )
