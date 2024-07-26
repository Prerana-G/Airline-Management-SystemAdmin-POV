# users.py
import streamlit as st


users = {
    "pragnya": {"password": "pragnya123"},
    "prerana": {"password": "prerana123"},
    "rakshitha":{"password":"rakshitha123"}
}

def authenticate(username, password):
    """Check if the provided username and password are correct."""
    if username in users and users[username]["password"] == password:
        return True
    return False

def login():
    """Display the login form and handle the login process."""
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if authenticate(username, password):
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.sidebar.success(f"Logged in as {username}")
        else:
            st.sidebar.error("Invalid username or password")

def logout():
    """Display the logout button and handle the logout process."""
    st.sidebar.title("Logout")
    if st.sidebar.button("Logout"):
        st.session_state["logged_in"] = False
        st.session_state["username"] = None
        st.sidebar.success("Logged out successfully")
