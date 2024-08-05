#pip install streamlit pymongo
#python.exe -m pip install --upgrade pip
#pip install streamlit pymongo
#cd \Globokas\ScoringPython

import streamlit as st
from pymongo import MongoClient, errors
import pandas as pd

# Intentar conectar a MongoDB
try:
    client = MongoClient("mongodb+srv://mhuaman:0AcY7h5YMFqWCvRS@innova.gfmnmzd.mongodb.net/?retryWrites=true&w=majority&appName=Innova")
    db = client["mhuaman"]
    collection = db["tb_tiendas"]
    st.success("Conexión a MongoDB exitosa")
except errors.ConnectionError:
    st.error("No se pudo conectar a MongoDB. Verifique la URL y las credenciales.")
    st.stop()  # Detiene la ejecución del script si no se puede conectar

# Título de la aplicación
st.title("Buscador de Tiendas")

# Entrada de texto para buscar por idCodigo
id_codigo = st.text_input("Ingrese el idCodigo para buscar la tienda:")

# Botón para ejecutar la búsqueda
if st.button("Buscar"):
    if id_codigo:
        result = collection.find_one({"idCodigo": id_codigo})
        if result:
            # Crear un DataFrame con los datos del resultado
            fields = [
                "idCodigo", "idPGY", "nombreTienda", "departamento", "provincia",
                "distrito", "direccion", "Longitud", "Fecha Instalación", "Fecha Baja",
                "tipoAgente", "estadoKasnet", "estadoPGY", "tipoPGY", "telefono_1",
                "telefono_2", "categoría", "region", "zona", "Operador Zonal", 
                "supervisor", "PlanMigr", "sectorZona", "latitude", "longitude",
                "Lista Negra", "¿Firmó?", "trxPGYNov", "trxPGYDic", "trxPGYEne",
                "trxPGYFeb", "trxPGYMar", "trxPGYActual", "Nov_23_Kas", "Dic_23_Kas",
                "Ene_24_Kas", "Feb_24_Kas", "Mar_24_Kas", "KasActual", "nov_23",
                "Dic_23", "En_24", "Feb_24", "Mar_24", "AvanceAntes", "avanActual",
                "Proyección", "Var_Mar_Abr", "saldo", "regMontoProm", "trxHidra",
                "comiHidra", "trxSEAL", "trxPgEfe", "Comi_PagEf", "trxTotalGE",
                "trxTotalGC", "trxGIROS", "trxTinka", "trxFullPagos", "metaOZ",
                "metaAg", "% AvanceFull", "Equipo", "¿Visitado?"
            ]

            # Convertir los datos a un DataFrame de pandas
            data = {field: [result.get(field, "N/A")] for field in fields}
            df = pd.DataFrame(data)

            # Mostrar los datos en una tabla
            st.dataframe(df, use_container_width=True)
        else:
            st.error("No se encontró ninguna tienda con el idCodigo proporcionado.")
    else:
        st.error("Por favor, ingrese un idCodigo.")

