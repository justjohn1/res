import streamlit as st

def show_contact_form():
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Send")

        if submit_button:
            if name and email and message:
                st.success(f"Form submitted (test mode):\nName: {name}\nEmail: {email}\nMessage: {message}")
                return True
            else:
                st.error("Please fill out all fields.")
    return False
