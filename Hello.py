import streamlit as st
from schoology import Schoology


st.title("Schoology App")
st.write("No idea what to do? Scroll to the instructions at the bottom of the page.")

KEY = st.text_input("Enter your API key:")
SECRET = st.text_input("Enter your secret:")

client = Schoology(key=KEY, secret=SECRET)
assignments = client.get('/v1/sections/{section_id}/assignments')