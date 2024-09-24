import streamlit as st
import sqlite3 as sqlite

def display_job(job):
    """Display job details in a visually appealing format."""
    st.subheader(f"JOB TITLE: {job[1]}")
    st.markdown(f"**Description:** {job[2]}")
    st.markdown(f"**Location:** {job[3]}")
    st.markdown(f"**Company:** {job[4]}")
    st.markdown(f"**Salary:** {job[5]}")
    st.markdown(f"**Posted On:** {job[6]}")
    st.markdown(f"**Type:** {job[7]}")
    st.markdown(f"**Requirements:** {job[8]}")
    st.markdown(f"**Contact:** {job[9]}")
    st.markdown("---")  

try:
    connection = sqlite.connect("datas.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()

    if jobs:
        st.title("Available Jobs")

        
        job_titles = sorted(set(job[1] for job in jobs))
        locations = sorted(set(job[3] for job in jobs))

        selected_title = st.selectbox("Select Job Title:", ["All"] + job_titles)
        selected_location = st.selectbox("Select Location:", ["All"] + locations)

        
        filtered_jobs = [
            job for job in jobs
            if (selected_title == "All" or job[1] == selected_title) and
               (selected_location == "All" or job[3] == selected_location)
        ]

        if filtered_jobs:
            cols = st.columns(2)  
            for idx, job in enumerate(filtered_jobs):
                with cols[idx % 2]:  
                    display_job(job) 
        else:
            st.write("No jobs found matching your criteria.")

    else:
        st.write("No jobs found.")

    cursor.close()
    connection.close()
except Exception as e:
    st.error(f"An error occurred: {e}")
