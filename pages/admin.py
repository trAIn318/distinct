#===============================================
# This web program by Maria Luznedy, hugo Fernando
# Nov 28/2024
# ver:1
# for: Hospitality.com
#=======================================================
import streamlit as st
from streamlit_extras.row import row

from streamlitPostgres.streamlitpostgres import cargarDatos


st.title("Admin Database")  # Press Ctrl+F8 to toggle the breakpoint.

#col1, col2, col3 = st.columns(3, gap="small", vertical_alignment="center")
st.write("")
st.write("")

#First datatable
#row1 = row([0.1, 0.9], vertical_align="center")
#row1.subheader("Roles")
#dfDatos_rol = cargarDatos('select * from Roles')
#row1.dataframe(dfDatos_rol, use_container_width=True)

#Second datatable
#row2 = row([0.1, 0.9], vertical_align="center")
#row2.subheader("Users", anchor=False)
#dfDatos_usr = cargarDatos('select * from users')
#row2.dataframe(dfDatos_usr, use_container_width=True)

#third datatable
#row3 = row([0.4, 0.6], vertical_align="center")
#row3.subheader("Users - Roles ", anchor=False)
#dfDatos_usr = cargarDatos('select * from user_roles')
#row3.dataframe(dfDatos_usr, use_container_width=True)
