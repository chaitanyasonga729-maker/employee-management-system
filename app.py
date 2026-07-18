import streamlit as st

from database import create_tables
from auth import create_admin, login

create_tables()
create_admin()

st.title("Employee Management System")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if login(username, password):
        st.success("Login Successful")
    else:
        st.error("Invalid Username or Password")