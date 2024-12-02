#===============================================
# This web program by Maria Luznedy, hugo Fernando
# Nov 28/2024
# ver:1
# for: Hospitality.com
#=======================================================

import streamlit as st

st.title("More Data")  # Press Ctrl+F8 to toggle the breakpoint.
from streamlitPostgres.streamlitpostgres import cargarDatos


dfDatos = cargarDatos('select * from users')
st.dataframe(dfDatos)

#conect = crate_ciente()
#test_func(conect)
#query(conect)

