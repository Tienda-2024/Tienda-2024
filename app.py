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
    # st.success("Conexión a MongoDB exitosa")
except errors.ConnectionError:
    st.error("No se pudo conectar a MongoDB. Verifique la URL y las credenciales.")
    st.stop()  # Detiene la ejecución del script si no se puede conectar

# CSS personalizado para el texto
st.markdown(
    """
    <style>
    .custom-input-label {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        display: block;
        margin-bottom: 10px;
    }
        .stTextInput>div>div>input {
        border: 2px solid #007bff;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Variable de texto
texto = "Buscador de tienda Kanset"

# Mostrar el texto con el estilo personalizado
st.markdown(f'<div class="custom-input-label">{texto}</div>', unsafe_allow_html=True)

# Entrada de texto para buscar por idCodigo
id_codigo = st.text_input(" ", placeholder="Ingrese el código de 6 dígitos", max_chars=6, key='id_codigo')

# Validar que el input solo contiene números y tiene exactamente 6 dígitos
if id_codigo.isdigit() and len(id_codigo) == 6:
    result = collection.find_one({"idCodigo": id_codigo})
    if result:
        # Dividir los campos en tres grupos
        fields_col1 = [
            "idCodigo", "idPGY", "nombreTienda", "departamento", "provincia",
            "distrito", "direccion"
        ]
        fields_col2 = [
            "Longitud", "tipoPGY", "telefono_1", "telefono_2", "categoría",
            "region", "zona"
        ]
        fields_col3 = [
            "Operador Zonal", "supervisor", "PlanMigr", "sectorZona", "latitude", 
            "longitude", "nov_23", "Dic_23", "En_24", "Feb_24", "Mar_24", 
            "AvanceAntes", "avanActual", "Proyección"
        ]

        col1, col2, col3 = st.columns(3)
        
        # Mostrar los campos en columnas
        with col1:
            for field in fields_col1:
                value = result.get(field, "N/A")
                st.markdown(f"<div class='stWrite'><strong>{field}:</strong> {value}</div>", unsafe_allow_html=True)
        
        with col2:
            for field in fields_col2:
                value = result.get(field, "N/A")
                st.markdown(f"<div class='stWrite'><strong>{field}:</strong> {value}</div>", unsafe_allow_html=True)
        
        with col3:
            for field in fields_col3:
                value = result.get(field, "N/A")
                st.markdown(f"<div class='stWrite'><strong>{field}:</strong> {value}</div>", unsafe_allow_html=True)
    else:
        st.error("No se encontró ninguna tienda con el idCodigo proporcionado")
elif id_codigo:
    if not id_codigo.isdigit():
        st.error("El código debe ser numérico")
    elif len(id_codigo) != 6:
        st.error("El código debe tener exactamente 6 dígitos")
