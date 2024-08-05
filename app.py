#pip install streamlit pymongo
#python.exe -m pip install --upgrade pip
#pip install streamlit pymongo
#cd \Globokas\ScoringPython


import streamlit as st
from pymongo import MongoClient, errors

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
            st.write("**Nombre de la Tienda:**", result.get("nombreTienda", "N/A"))
            st.write("**Departamento:**", result.get("departamento", "N/A"))
            st.write("**Provincia:**", result.get("provincia", "N/A"))
            st.write("**Distrito:**", result.get("distrito", "N/A"))
            st.write("**Categoría:**", result.get("categoría", "N/A"))
            st.write("**Región:**", result.get("region", "N/A"))
            st.write("**Zona:**", result.get("zona", "N/A"))
            st.write("**Transacciones FullPagos:**", result.get("trxFullPagos", "N/A"))
        else:
            st.error("No se encontró ninguna tienda con el idCodigo proporcionado.")
    else:
        st.error("Por favor, ingrese un idCodigo.")
