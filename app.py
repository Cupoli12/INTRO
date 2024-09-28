import streamlit as st
from PIL import Image

# Custom CSS for color and styling
st.markdown("""
    <style>
    /* Background color */
    .stApp {
        background-color: #f0f8ff;
        color: #333;
    }

    /* Title and headers */
    h1 {
        color: #ff6347;
        font-family: 'Comic Sans MS', cursive;
    }
    h2 {
        color: #6a5acd;
        font-family: 'Lucida Console', monospace;
    }

    /* Text input styling */
    .stTextInput > div > div {
        background-color: #faf0e6;
        color: #000;
        border: 2px solid #4682b4;
        padding: 5px;
        font-family: 'Courier New', Courier, monospace;
        font-size: 16px;
    }

    /* Subheader and checkboxes */
    .stCheckbox, .stRadio {
        color: #4682b4;
    }

    /* Image border */
    img {
        border: 5px solid #ff69b4;
        border-radius: 15px;
        box-shadow: 0px 0px 20px #4682b4;
    }

    /* Column customization */
    [data-testid="column"] {
        border: 2px dashed #ff6347;
        border-radius: 10px;
        padding: 10px;
        background-color: #e6e6fa;
    }

    /* Sidebar customization */
    .css-1lcbmhc {
        background-color: #ffe4e1;
        border: 2px solid #ff4500;
        border-radius: 10px;
        padding: 10px;
    }

    /* Button styling */
    .stButton > button {
        background-color: #ff69b4;
        color: #fff;
        font-size: 18px;
        padding: 10px;
        border: 2px solid #6a5acd;
        border-radius: 10px;
        box-shadow: 2px 2px 5px #4682b4;
    }
    .stButton > button:hover {
        background-color: #ff4500;
        border-color: #4682b4;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit content
st.title("Mi primera página")
st.header("Hola, ¿cómo va todo?")
st.write("🎨 Disfruta del contenido de esta página 🎨")

image = Image.open("gatopan.jpg")
st.image(image, caption="Gatopan 🐱", use_column_width=True)

texto = st.text_input("Escribe algo ✍️", "Este es mi texto")
st.write("El texto escrito es:", f"**{texto}**")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🌟 Primera columna")
    st.write("🌟 Las interfaces multimodales mejoran la experiencia de usuario")
    resp = st.checkbox("Estoy de acuerdo 🤝")
    if resp:
        st.success("¡Correcto! 🎉")

with col2:
    st.subheader("🌟 Segunda columna")
    modo = st.radio("¿Cuál es la modalidad principal de tu interfaz?", ("Visual 👁️", "Auditiva 👂", "Táctil ✋"))
    if modo == "Visual 👁️":
        st.write("La vista es fundamental para tu interfaz 👀")
    if modo == "Auditiva 👂":
        st.write("La audición es fundamental para tu interfaz 🎧")
    if modo == "Táctil ✋":
        st.write("El tacto es fundamental para tu interfaz 🖐️")

st.subheader("Uso de botones 🎮")
if st.button("¡Presiona el botón!"):
    st.balloons()
    st.success("¡Gracias por presionar! 🎉")
else:
    st.info("Aún no has presionado el botón. ¡Inténtalo! 😊")

# Sidebar customization
with st.sidebar:
    st.subheader("🔧 Configura la modalidad")
    mod_radio = st.radio(
        "Escoge la modalidad a usar:",
        ("Visual 👁️", "Auditiva 👂", "Háptica ✋")
    )
    st.write(f"Has seleccionado: **{mod_radio}**")
