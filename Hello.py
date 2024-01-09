import streamlit as st
import schoolopy


st.title("Schoology App")
st.write("No idea what to do? Scroll to the instructions at the bottom of the page.")

KEY = st.text_input("Enter your API key:")
SECRET = st.text_input("Enter your secret:")

# Two-legged
sc = schoolopy.Schoology(schoolopy.Auth(KEY, SECRET))
sc.get_feed()
