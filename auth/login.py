import streamlit as st
import json
import hashlib

def login():
    st.sidebar.title("🔐 Login")

    with open("auth/users.json") as f:
        users = json.load(f)

    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        if username in users and users[username] == hash_password(password):
            st.session_state["authenticated"] = True
            return True
        else:
            st.error("Invalid credentials")
            return False

    return st.session_state.get("authenticated", False)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
