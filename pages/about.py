#===============================================
# This web program by Maria Luznedy, hugo Fernando
# Nov 28/2024
# ver:1
# for: Hospitality.com
#=======================================================

import streamlit as st
from streamlit_extras.row import row
from forms.contact import contact_form

@st.dialog("Contact Me")


def show_contact_form():
    contact_form()


#st.markdown("""
#-------------------------------------------------------------------------------------------------------------
#""", unsafe_allow_html=True)

st.markdown('''# **Hospitality Courses**
The best onilie hospitality coures *Distinct*.
''')


# --- HERO SECTION ---

col1, col2, col3 = st.columns([0.7,0.27,0.03], gap="small", vertical_alignment="top") # Maja las columnas de la pagina
col7, col8 = st.columns([0.7, 0.3], gap="small", vertical_alignment="top")  # maneja los botones al comienzo

with col1:

    row1 = row(1, vertical_align="center")
    row1.image("./img/service.jpeg", width=700)
    row2 = row(1)
    row2.write("")
    row2.header("The Best Courses")
    col4, col5, col6 = st.columns([0.3, 0.3, 0.4], gap="small", vertical_alignment="top")


    with col4:
        #col4.header("bartender course")

        col4.image("./img/bartender.jpg")
        col4.markdown("###### Bartender Course by [Distinct](https://youtu.be/IWs2NZpQPQE)")
        col4.write("""This is a course of real world bartending experience, from real hospitality professionals across the industry. """)

    with col5:

        col5.image("./img/hotelbanquet.jpg")
        col5.markdown("###### Hotel Banquetes Course by [Distinct](https://youtu.be/IWs2NZpQPQE)")
        col5.write("""This comprehensive online course will equip you with the skills and knowledge necessary to plan and execute successful banquets. From menu planning and event design to staff management and client relations, you'll learn everything you need to know to create unforgettable dining experiences.""")
    with col6:

        col6.image("./img/housekeeper.jpeg")
        col6.markdown("###### Housekeeper Course by [Distinct](https://youtu.be/IWs2NZpQPQE)")
        col6.write("""Highly efficient Housekeeping Attendant with a strong work ethic. Proven ability to complete assigned tasks on time and to a high standard. Skilled in time management and organization. Committed to maintaining a clean and welcoming environment for guests. """)
with col2:
    with st.container():

        row4 = row(1, vertical_align="center")
        row4.link_button("Conect to Moodle","https://moodle.traindistincthospitality.com/login/index.php", type="primary",use_container_width=True)
        if row4.button("✉️ Contact Us", use_container_width=True):
            show_contact_form()

        row4.markdown("### Distinct")
        row4.write(
            "Train by Distinct Hospitality Our training and upskilling platform for the hospitality and service industries.")

        row4.write("\n")
        row4.markdown("##### For Individuals")
        row4.write(
            """
            - Access to learning libraries, videos and industry-specific content
            - Engage with podcast interviews, seminars, and virtual learning labs
            - Personalized chats for continuous learning and improvement
            - Excellent team-player and displaying a strong sense of initiative on tasks
            """
         )

    # --- Organizations ---

        row4.write("\n")
        row4.markdown("##### For Organizations")
        row4.write(
            """
            - Services for hiring, upskilling, and recertifications
             - Custom workforce aptitude reviews based on your standards
            - HR tools for sourcing, evaluating, and hiring
             - Management tools for consistent team training and development.
            """
            )




