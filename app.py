import streamlit as st
from PIL import Image
st.title("Mi primera página")
st.header("Hola, como va todo")
st.write("Diferente tipo de letra")


image = Image.open("gatopan.jpg")
st.image(image, caption = "gatopan")
