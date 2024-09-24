import os
import sqlite3
import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI()

# Connect to SQLite database
def get_database_connection():
    conn = sqlite3.connect('resumes.db')  # Update with your database path
    return conn

# Function to filter resumes based on user input
def filter_resumes(criteria):
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM resumes WHERE skills LIKE ? OR experience LIKE ?", (f'%{criteria}%', f'%{criteria}%'))
    results = cursor.fetchall()
    conn.close()
    return results

# Streamlit app title
st.title("Resume Filter App")

# Session state to store messages
if 'messages' not in st.session_state:
    st.session_state.messages = []

# User input box for filtering resumes
user_input = st.text_input("Enter skills or experience to filter resumes:")

# Button to filter resumes
if st.button("Filter Resumes"):
    if user_input:
        resumes = filter_resumes(user_input)
        if resumes:
            st.write("### Filtered Resumes")
            for resume in resumes:
                st.write(f"**ID**: {resume[0]}")
                st.write(f"**Name**: {resume[1]}")
                st.write(f"**Skills**: {resume[2]}")
                st.write(f"**Experience**: {resume[3]}")
                st.write("---")
        else:
            st.write("No resumes found matching your criteria.")

# Display message history if needed
if st.session_state.messages:
    st.write("### Message History")
    for msg in st.session_state.messages:
        if msg['role'] == 'user':
            st.write(f"**User**: {msg['content']}")
        else:
            st.write(f"**Assistant**: {msg['content']}")
