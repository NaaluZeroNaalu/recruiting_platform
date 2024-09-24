import sqlite3
import streamlit as st
import openai

# Initialize OpenAI client

#operators - it is an symbol it is used to perform mathematial or logical operations
#operator types
#arithmetic opertor - +, -, *, /, ^, %%(modulas division), %/%(integer division)
#assignment operator - =, <-, ->, ->>, <<-
#comparison operator - ==, <, >, <=, >=, !=
#logical operator = &&, ||, !
#miscellaneous operator - : (series), %*% (matrix multiplication), %in%

# Connect to SQLite database
def get_database_connection():
    conn = sqlite3.connect('resumes.db')  # Update with your database path
    return conn

# Function to filter resumes based on user input
def filter_resumes(criteria):
    conn = get_database_connection()
    cursor = conn.cursor()
    
    # SQL query to fetch resumes based on criteria from the 'employer' table
    cursor.execute("SELECT id, name, skills, experience, resume_blob FROM employer WHERE skills LIKE ? OR experience LIKE ?", (f'%{criteria}%', f'%{criteria}%'))
    results = cursor.fetchall()
    conn.close()
    return results

# Function to decode BLOB data
def decode_blob(blob_data):
    return blob_data.decode('utf-8')  # Adjust based on your data format

# Streamlit app title
st.title("Employer Resume Filter App")

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
                
                # Decode and display the resume content
                resume_content = decode_blob(resume[4])  # Assuming the BLOB is at index 4
                st.text_area("Resume Content", resume_content, height=200)
                st.write("---")
        else:
            st.write("No resumes found matching your criteria.")
