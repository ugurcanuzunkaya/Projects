import streamlit as st
from send_email import send_email

st.set_page_config(page_title="Contact Me", page_icon="✉️", layout="wide", initial_sidebar_state="auto")

st.header("Contact Me")

st.write("Feel free to reach out for collaboration or inquiries! 😄")

with st.form(key="contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    raw_message = st.text_area("Your Message")
    button = st.form_submit_button(label="Submit")
    
    
    if button:
        send_email(f"Subject: New Message from portfolio website!\n\nName: {name}\nEmail: {email}\nMessage: {raw_message}")
        
        st.info(f"Thank you for your message {name}! I'll get back to you shortly.")