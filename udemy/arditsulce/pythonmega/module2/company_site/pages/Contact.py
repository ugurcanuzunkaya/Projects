import streamlit as st
from send_email import send_email
import pandas as pd

st.set_page_config(
    page_title="Best Company",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="auto",
)

st.header("Contact Us")

st.write("Feel free to reach out for collaboration or inquiries! 😄")

df = pd.read_csv("topics.csv", sep=",")

with st.form(key="contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    topic = st.selectbox("Mail Topic", df["topic"].tolist())
    raw_message = st.text_area("Your Message")

    if button := st.form_submit_button(label="Submit"):
        send_email(
            f"Subject: New Message from Best Company website!\n\nName: {name}\nEmail: {email}\nMessage: {raw_message}"
        )

        st.info(f"Thank you for your message {name}! We'll get back to you shortly.")
