#pip install streamlit pymongo
#python.exe -m pip install --upgrade pip
#pip install streamlit pymongo
#cd \Globokas\ScoringPython

import streamlit as st
from pymongo import MongoClient, errors

# Estilo CSS para mejorar la apariencia y ocultar elementos
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
        border-radius: 3px;
        padding: 10px;
        height: 40px;  /* Ajusta la altura del botón */
        margin-left: 10px;  /* Agrega un margen a la izquierda del botón */
        margin-top: 27px;  /* Agrega un margen superior para alinear con el input */
    }
    .stButton>button:hover {
        background-color: #0056b3;
        color: white;
    }
    .stTextInput>div>div>input {
        border: 2px solid #007bff;
        border-radius: 5px;
        padding: 10px;
        /*height: 40px; Ajusta la altura del input para que coincida con el botón */
        /*margin-top: 5px; Agrega un margen superior para alinear con el botón */
    }
    /* Estilo para el título de la aplicación */
    .stTitle {
        font-size: 20px;  /* Disminuye el tamaño del texto del título */
    }
    /* Ocultar ícono de GitHub y menú de opciones, mostrar solo Share */
    header .decoration, header [data-testid="stDecoration"] {
        display: none;
    }
    header [data-testid="stToolbar"] {
        display: flex;
        justify-content: space-between;
    }
    header [data-testid="stToolbar"] > div:nth-child(2) {
        display: none;
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
    #st.success("Conexión a MongoDB exitosa")
except errors.ConnectionError:
    st.error("No se pudo conectar a MongoDB. Verifique la URL y las credenciales.")
    st.stop()  # Detiene la ejecución del script si no se puede conectar

# Título de la aplicación
st.title("Buscador de Tiendas")

# Columnas para input y botón
col1, col2 = st.columns([2, 2])

# Input en la primera columna con placeholder y etiqueta oculta
with col1:
    id_codigo = st.text_input("Código de Tienda", placeholder="Ingrese el idCodigo para buscar la tienda", label_visibility="hidden")

# Botón en la segunda columna
with col2:
    buscar = st.button("Buscar")

# Botón para ejecutar la búsqueda
if buscar:
    if id_codigo:
        result = collection.find_one({"idCodigo": id_codigo})
        if result:
            # Mostrar los campos disponibles
            fields = [
                "idCodigo", "idPGY", "nombreTienda", "departamento", "provincia",
                "distrito", "direccion", "Longitud", "Fecha Instalación", "Fecha Baja",
                "tipoAgente", "estadoKasnet", "estadoPGY", "tipoPGY", "telefono_1",
                "telefono_2", "categoría", "region", "zona", "Operador Zonal", 
                "supervisor", "PlanMigr", "sectorZona", "latitude", "longitude","nov_23",
                "Dic_23", "En_24", "Feb_24", "Mar_24", "AvanceAntes", "avanActual",
                "Proyección", "Var_Mar_Abr", "saldo", "regMontoProm"
            ]
            
            for field in fields:
                value = result.get(field, "N/A")
                st.write(f"**{field}:**", value)
        else:
            st.error("No se encontró ninguna tienda con el idCodigo proporcionado.")
    else:
        st.error("Por favor, ingrese un idCodigo.")
