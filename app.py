#pip install streamlit pymongo
#python.exe -m pip install --upgrade pip
#pip install streamlit pymongo
#cd \Globokas\ScoringPython

import streamlit as st
from pymongo import MongoClient, errors

# Estilo CSS para mejorar la apariencia
st.markdown(
    """
    <style>
    .reportview-container {
        background: #f0f2f6;
    }
    .css-1d391kg {
        background-color: #f0f2f6;
    }
    .css-10trblm {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
    }
    .stButton>button {
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px;
        height: 40px; /* Ajusta la altura del botón */
    }
    .stButton>button:hover {
        background-color: #0056b3;
        color: white;
    }
    .stTextInput>div>div>input {
        border: 2px solid #007bff;
        border-radius: 5px;
        padding: 10px;
        height: 40px; /* Ajusta la altura del input */
    }
    .stWrite {
        margin-bottom: 5px; /* Reduce el espacio entre los campos */
    }
    /* Estilo para alinear el título y el input en la parte superior */
    .stHeader {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .stHeader .stTitle {
        margin: 0;
        font-size: 24px;
    }
    .stHeader .stTextInput {
        flex-grow: 1;
        margin-right: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Intentar conectar a MongoDB
try:
    client = MongoClient("mongodb+srv://mhuaman:0AcY7h5YMFqWCvRS@innova.gfmnmzd.mongodb.net/?retryWrites=true&w=majority&appName=Innova")
    db = client["mhuaman"]
    collection = db["tb_tiendas"]
    # st.success("Conexión a MongoDB exitosa")
except errors.ConnectionError:
    st.error("No se pudo conectar a MongoDB. Verifique la URL y las credenciales.")
    st.stop()  # Detiene la ejecución del script si no se puede conectar

# Título de la aplicación y entrada en la parte superior
st.markdown(
    """
    <div class="stHeader">
        <div class="stTitle">Agentes Kasnet</div>
        <div class="stTextInput">{}</div>
        <div class="stButton">{}</div>
    </div>
    """.format(
        st.text_input("Ingrese el idCodigo para buscar la tienda"),
        st.button("Buscar")
    ),
    unsafe_allow_html=True
)

# Botón para ejecutar la búsqueda
if st.button("Buscar"):
    if id_codigo:
        result = collection.find_one({"idCodigo": id_codigo})
        if result:
            # Mostrar los campos disponibles
            fields = [
                "idCodigo", "idPGY", "nombreTienda", "departamento", "provincia",
                "distrito", "direccion", "Longitud", "tipoPGY", "telefono_1",
                "telefono_2", "categoría", "region", "zona", "Operador Zonal", 
                "supervisor", "PlanMigr", "sectorZona", "latitude", "longitude",
                "nov_23",
                "Dic_23", "En_24", "Feb_24", "Mar_24", "AvanceAntes", "avanActual",
                "Proyección"
            ]
            
            for field in fields:
                value = result.get(field, "N/A")
                st.markdown(f"<div class='stWrite'><strong>{field}:</strong> {value}</div>", unsafe_allow_html=True)
        else:
            st.error("No se encontró ninguna tienda con el idCodigo proporcionado.")
    else:
        st.error("Por favor, ingrese un idCodigo.")
