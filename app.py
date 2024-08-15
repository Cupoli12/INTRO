import streamlit as st
from PIL import Image
st.title("Mi primera página")
st.header("Hola, como va todo")
st.write("Diferente tipo de letra")

image = Image.open("gatopan.jpg")
st.image(image, caption = "gatopan")

texto = st.text_input("Escribe algo" , "Este es mi texto")
st.write("El texto escrito es" , texto)

col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia de ususario")
  resp = st.checkbox("Estoy de acuerdo")
  if resp:
    st.write("Correcto!")

with col2:
  st.subheader("Esta es la segunda columna")
  modo=st.radio("Que modalidad es la principal de tu interfaz", ("Visual","Auditiva","Táctil"))
  if modo == "Visual":
    st.write("La vista es fundamental para tu interfaz")
  if modo == "Auditiva":
    st.write("La audición es fundamental para tu interfaz")
  if modo == "Táctil":
    st.write("El tacto es fundamental para tu interfaz")
