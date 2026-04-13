#####Gen 2
import streamlit as st
import os
from forms.contact import show_contact_form
from b.b_manager import enforce_auth
st.set_option('client.showErrorDetails', False)

# Call this function at the start of your app
enforce_auth()

# ✅ Move this to the VERY FIRST Streamlit command
st.set_page_config(page_title="Your Portfolio", layout="wide")

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = "About Me"

if 'show_form' not in st.session_state:
    st.session_state.show_form = False

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))


@st.dialog("Contact Me")
def display_contact_form():
    if st.session_state.show_form:
        show_contact_form()


# --- NAVIGATION SETUP ---
col1, col2 = st.columns([1, 3])  # Adjust column widths as needed

with col1:
    st.header("Navigation")

    button_style = """
        <style>
        .stButton > button {
            width: 100%;  /* Make buttons full width */
            height: 60px; /* Set a fixed height */
            font-size: 16px; /* Increase font size */
            text-align: center; /* Center text */
            padding: 10px; /* Add padding */
        }
        </style>
    """
    st.markdown(button_style, unsafe_allow_html=True)

    if st.button("About Me"):
        st.session_state.page = "About Me"
        st.session_state.show_form = False

    if st.button("Code project 1: Advanced Malware Sacnner (Gen 3)"):
        st.session_state.page = "Project 1"
        st.session_state.show_form = False

    if st.button("Code accomplishment 1:\n\t\t Digital Boomerang"):
        st.session_state.page = "Project 2"
        st.session_state.show_form = False

    if st.button("Code accomplishment 2: SOC Phish Automation"):
        st.session_state.page = "Project 3"
        st.session_state.show_form = False

    if st.button("Code project 2: AI Finance Automation"):
        st.session_state.page = "Project 4"
        st.session_state.show_form = False


# ✅ Check if the included files contain `st.set_page_config()`
def safe_exec(file_path):
    with open(file_path, "r") as file:
        file_content = file.read()

        # 🚨 Prevent re-executing `st.set_page_config()` again
        if "st.set_page_config" in file_content:
            print(f"⚠️ Warning: `st.set_page_config()` found in {file_path}. Skipping execution.")
            return

        exec(file_content)


with col2:
    if st.session_state.page == "About Me":
        st.title("About Me")
        safe_exec(os.path.join(current_dir, "views", "about_me.py"))

    elif st.session_state.page == "Project 1":
        safe_exec(os.path.join(current_dir, "views", "yara_scanner.py"))

    elif st.session_state.page == "Project 2":
        safe_exec(os.path.join(current_dir, "views", "digital_boomerang.py"))

    elif st.session_state.page == "Project 3":
        safe_exec(os.path.join(current_dir, "views", "auto_phisher.py"))

    elif st.session_state.page == "Project 4":
        safe_exec(os.path.join(current_dir, "views", "AI_finance_project.py"))

# Display contact form if needed
if st.session_state.show_form:
    display_contact_form()
