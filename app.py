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
except errors.ConnectionError:
    st.error("No se pudo conectar a MongoDB. Verifique la URL y las credenciales.")
    st.stop()

# CSS personalizado para mejorar el diseño
st.markdown(
    """
    <style>
    .custom-input-label {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        color: #4A90E2;
         margin-bottom: 10px;
    }
    .stTextInput>div>div>input {
        border: 1px solid #007bff;
        border-radius: 4px;
        font-size: 13px;
    }
    .stWrite {
        margin-bottom: 0px;
        color: #333;
         font-size: 13px;
    }
    .stWrite strong {
        color: #007bff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título
#st.markdown(f'<div class="custom-input-label">Buscador de tienda Kanset</div>', unsafe_allow_html=True)
Texto = "**BUSCADOR DE AGENTES KASNET**"
id_codigo = st.text_input(Texto, placeholder="Ingrese el código de 6 dígitos", max_chars=6, key='id_codigo')

# Diccionario de renombrado de campos
field_names = {
    "idCodigo": "Id agente",
    "Tienda": "Comercio",
    "Coordinador": "Coordinador",
    "Zona": "Zona",
    "TipoPGY": "PAGAYA",
    "trxPGYAgt": "Agosto 23",
    "trxPGYSept": "Septiembre 23",
    "trxPGYOct": "Octubre 23",
    "trxPGYNov": "Noviembre 23",
    "trxPGYDic": "Diciembre 23",
    "trxPGYEne": "Enero 24",
    "trxPGYFeb": "Febrero 24",
    "trxPGYMar": "Marzo 24",
    "trxPGYAbr": "Abril 24",
    "trxPGYMay": "Mayo 24",
    "trxPGYJun": "Junio 24",
    "trxPGYJul": "Julio 24",
    "trxPGYActual": "Avance agosto",
    "idPGY": "Terminal PGY",
    "Provincia": "Provincia",
    "Distrito": "Distrito",
    "Categoría": "Categoría",
    "Operador Zonal": "Operador Zonal",
    "Tipo_Agente": "KASNET",

    "Agt_23_Kas": "Agosto 23",
    "Sept_23_Kas": "Septiembre 23",
    "Oct_23_Kas": "Octubre 23",
    "Nov_23_Kas": "Noviembre 23",
    "Dic_23_Kas": "Diciembre 23",
    "Ene_24_Kas": "Enero 24",
    "Feb_24_Kas": "Febrero 24",
    "Mar_24_Kas": "Marzo 24",
    "Abr_24_Kas": "Abril 24",
    "May_24_Kas": "Mayo 24",
    "Jun_24_Kas": "Junio 24",
    "Jul_24_Kas": "Julio 24",
    "KasActual": "Avance agosto",
    
    "Departamento": "Departamento",
    "Región": "Región",
    "Supervisor": "Nombre del Supervisor",
    "Motivo_Garantía": "Motivo de Garantía",
    "Monto_Garantía": "Monto de Garantía",
    "PlanMigr": "Plan de Migración",
    "Agt_23": "Total Agt 23",
    "Sept_23": "Total Spt 23",
    "Oct_23": "Total Oct 23",
    "nov_23": "Total Nov 23",
    "Dic_23": "Total Dic 23",
    "En_24": "Total Ene 24",
    "Feb_24": "Total Feb 24",
    "Mar_24": "Total Mar 24",
    "Abr_24": "Total Abr 24",
    "May_24": "Total May 24",
    "Jun_24": "Total Jun 24",
    "Jul_24": "Total Jul 24",
    "avanActual": "Total avance",
    "Te_Extendemos_la_grati": "Te extendemos la grati",
    "Meta": "Meta",
    " % Avance": "Porcentaje de Avance"
}

# Validar que el input solo contiene números y tiene exactamente 6 dígitos
if id_codigo.isdigit() and len(id_codigo) == 6:
    result = collection.find_one({"idCodigo": id_codigo})
    if result:
        # Dividir los campos en tres grupos
        fields_col1 = [
            "idCodigo", "Tienda",  "Región", "Zona","Operador Zonal",  
            "TipoPGY", "trxPGYAgt", "trxPGYSept","trxPGYOct", "trxPGYNov",
            "trxPGYDic", "trxPGYEne","trxPGYFeb", "trxPGYMar","trxPGYAbr", "trxPGYMay",
            "trxPGYJun","trxPGYJul","trxPGYActual","Te_Extendemos_la_grati", 
        ]
        fields_col2 = [
            "idPGY","Categoría", "Coordinador","Supervisor",
            "Tipo_Agente","Agt_23_Kas","Sept_23_Kas","Oct_23_Kas","Nov_23_Kas",
            "Dic_23_Kas","Ene_24_Kas","Feb_24_Kas","Mar_24_Kas", "Abr_24_Kas","May_24_Kas", 
            "Jun_24_Kas", "Jul_24_Kas","KasActual","Meta"
        ]
        fields_col3 = [
            "Departamento","Provincia", "Distrito", "Motivo_Garantía", "Monto_Garantía",
            "PlanMigr","Agt_23","Sept_23","Oct_23", "nov_23","Dic_23", "En_24",
            "Feb_24", "Mar_24","Abr_24","May_24","Jun_24", "Jul_24",
            "avanActual"," % Avance"
        ]

        col1, col2, col3 = st.columns(3)

        # Mostrar los campos en columnas con nombres renombrados
        for col, fields in zip([col1, col2, col3], [fields_col1, fields_col2, fields_col3]):
            with col:
                for field in fields:
                    display_name = field_names.get(field, field)  # Obtener el nombre del campo renombrado
                    value = result.get(field, "N/A")
                    st.markdown(f"<div class='stWrite'><strong>{display_name}:</strong> {value}</div>", unsafe_allow_html=True)
    else:
        st.error("No se encontró ninguna tienda con el código proporcionado")
elif id_codigo:
    if not id_codigo.isdigit():
        st.error("El código debe ser numérico")
    elif len(id_codigo) != 6:
        st.error("El código debe tener exactamente 6 dígitos")
