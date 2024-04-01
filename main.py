import streamlit as st
from PIL import Image

def main():
    st.title("Visualizador de Imagen del Sol")
    st.write("Carga una imagen del sol y mírala aquí!")

    uploaded_file = st.file_uploader("Cargar imagen", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Mostrar la imagen cargada
        image = Image.open(uploaded_file)
        st.image(image, caption="Imagen del Sol", use_column_width=True)

if __name__ == "__main__":
    main()
