import streamlit as st
import schoolopy


st.title("Schoology App")
st.write("No idea what to do? Scroll to the instructions at the bottom of the page.")

KEY = st.text_input("Enter your API key:")
SECRET = st.text_input("Enter your API secret:")

sc = schoolopy.Schoology(schoolopy.Auth(KEY, SECRET))
auth = schoolopy.Auth(KEY, SECRET)

# Instantiate the API wrapper
sc = schoolopy.Schoology(auth)

# Get a list of all courses
courses = sc.get_courses()

# Print the name of each course
for course in courses:
    print(course['course_title'])