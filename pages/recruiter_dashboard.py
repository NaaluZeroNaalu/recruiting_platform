import streamlit as st
import sqlite3 as sqlite

@st.dialog("Edit Details")
def Editdetails(detail):
    if detail == "about":
        st.write("about")
        new_about = st.text_area("Enter your new about information:")
        if st.button("Update About"):
            try:
                connection = sqlite.connect("datas.db")
                cursor = connection.cursor()
                
                cursor.execute("UPDATE recruiter SET about = ? WHERE email = ?", (new_about, st.session_state.id_name))
                connection.commit()
                st.success("altered successfull")    
                cursor.close()
                connection.close()
            
            except Exception as e:
                st.write(f"An error occurred: {e}")

    if detail == "skills":
        st.write("about")
        new_skills = st.text_area("Enter your skills:")
        if st.button("Update Skiils"):
            try:
                connection = sqlite.connect("datas.db")
                cursor = connection.cursor()
                
                cursor.execute("UPDATE recruiter SET skills = ? WHERE email = ?", (new_skills, st.session_state.id_name))
                connection.commit()
                st.success("altered successfull")    
                cursor.close()
                connection.close()
            
            except Exception as e:
                st.write(f"An error occurred: {e}")

    if detail == "contact":
        st.write("contact")
        new_contact = st.text_area("Enter your contact number:")
        if st.button("Update Contact"):
            try:
                connection = sqlite.connect("datas.db")
                cursor = connection.cursor()
                
                cursor.execute("UPDATE recruiter SET skills = ? WHERE email = ?", (new_contact, st.session_state.id_name))
                connection.commit()
                st.success("contact updated successfully")    
                cursor.close()
                connection.close()
            
            except Exception as e:
                st.write(f"An error occurred: {e}")

    if detail == "email":
        st.write("Email")
        new_email = st.text_area("Enter your Email:")
        if st.button("Update Email"):
            try:
                connection = sqlite.connect("datas.db")
                cursor = connection.cursor()
         
                cursor.execute("UPDATE recruiter SET email = ? WHERE email = ?", (new_email, st.session_state.id_name))
                st.session_state.id_name = new_email
                connection.commit()
                st.success("email updated successfully")    
                cursor.close()
                connection.close()
            
            except Exception as e:
                st.write(f"An error occurred: {e}")



                
def download_resume(email):
    try:
        connection = sqlite.connect("datas.db")
        cursor = connection.cursor()
        
        cursor.execute("SELECT resume FROM employer WHERE email = ?", (email,))
        resume = cursor.fetchone()

        if resume and resume[0]:
            return resume[0]  # Return the resume BLOB
        else:
            st.error("No resume found.")
            return None
    except Exception as e:
        st.error(f"An error occurred: {e}")
    finally:
        cursor.close()
        connection.close()


try:
    connection = sqlite.connect("datas.db")
    cursor = connection.cursor()
    a = st.session_state.id_name
    cursor.execute("SELECT * FROM recruiter WHERE email = ? ", (a,))
    user = cursor.fetchall()

    if user:
        st.write(user[0][0])
        if user[0][6] == None or user[0][6] == "":
            if st.button("Tell about something you"):
                Editdetails("about")
        else:
            if st.button(user[0][6],help="Edit?"):
                Editdetails("about")

        if user[0][2] == None or user[0][2] == "":
            if st.button("Add skills"):
                Editdetails("skills")
        else:
            st.button(user[0][2])

        if user[0][2] == None or user[0][3] == "":
            if st.button("Add contact"):
                Editdetails("contact")
        else:
            st.button(user[0][3])
      

        if user[0][2] == None or user[0][4] == "":
            if st.button("Add email"):
                Editdetails("email")
        else:
            if st.button(user[0][4]):
                Editdetails("email")



    else:
       st.write("empty")

    cursor.close()
    connection.close()
except Exception as e:
    st.error(f"An error occurred: {e}")

st.page_link("pages/job_post.py",label="POST A JOB")



