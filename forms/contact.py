import re
import streamlit as st
import requests

WEBHOOK_URL = "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjYwNTZhMDYzZTA0MzI1MjZiNTUzNTUxMzIi_pc"

# Inject custom CSS
st.markdown("""
    <style>
    /* Style the whole form box */
    .stForm {
        background-color: #f9f9f9;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    }

    /* Improve spacing between inputs */
    .stTextInput, .stTextArea {
        margin-bottom: 15px;
    }

    /* Style submit button */
    .stForm button[kind="primary"] {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 8px 20px;
        font-size: 16px;
        font-weight: bold;
        transition: 0.3s;
    }

    .stForm button[kind="primary"]:hover {
        background-color: #45a049;
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)


def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_pattern, email) is not None


def contact_form():
    with st.form("Contact Form"):
        fname = st.text_input("First Name")
        lname = st.text_input("Last Name")
        email = st.text_input("Email Address")
        message = st.text_input("Your Message")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            if not WEBHOOK_URL:
                st.error("Email Service is not set up. Please try again later", icon="📧")
                st.stop()

            if not fname:
                st.error("Please enter your first name", icon="👤")
                st.stop()

            if not lname:
                st.error("Please enter your last name", icon="👤")
                st.stop()

            if not email:
                st.error("Please provide your email address", icon="📧")
                st.stop()

            if not is_valid_email(email):
                st.error("Please enter a valid email address", icon="📧")
                st.stop()

            if not message:
                st.error("Please write your message", icon="💬")
                st.stop()

            # Prepare payload and send it to the specified WEB HOOK URL
            data = {"email": email, "fname": fname, "lname": lname, "message": message}
            response = requests.post(WEBHOOK_URL, json=data)

            if response.status_code == 200:
                st.success("Your message has been sent successfully! I will get back to you soon. 📩", icon="✅")
            else:
                st.error("There was an error sending your message. Please try again later.💬", icon="🚫")


# Call the form
#contact_form()


