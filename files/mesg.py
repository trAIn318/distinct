import streamlit as st
from oauth2client.service_account import ServiceAccountCredentials
import gspread

directorio_local ='D:\Master\projects\distinct\.streamlit/'

 #Authorize the API
scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
    ]


directorio =''

def save_arch(name,email,mesg):

    file_name = directorio_local+'client_key.json'
    creds = ServiceAccountCredentials.from_json_keyfile_name(file_name,scope)
    client = gspread.authorize(creds)

    cadena = name + ',' + email+ ','+mesg

    output = directorio + 'contacto'
    # Fetch the sheet
    sheet = client.open(output).sheet1

    # cuentra la ulitma fila de la hoja de calculo
    ult_fila = 2
    ult_fila = sheet.row_count

    # Imprime el numero de fila en la pantalla
    st.write("Registro a procesar :", ult_fila)

    # asigna el numero de registro a la cadena con los valores
    cadena = str(ult_fila) + cadena

    # Genera una lista con los campos que se van a grabar en el archivo
    row = cadena.split(sep=',')
    num_filas = 2

    # Inserta el registro completo
    sheet.insert_row(row, num_filas)
