import streamlit as st
from PIL import Image
import numpy as np
import cv2

def main():
    st.title("Visualizador de Imagen del Sol")
    st.write("Carga una imagen del sol y mírala aquí!")

    uploaded_file = st.file_uploader("Cargar imagen", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
    # Mostrar la imagen cargada
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen del Sol", use_column_width=True)

    
    if uploaded_file is not None:
        # Convertir la imagen cargada a una matriz numpy
        image = Image.open(uploaded_file)
        image_np = np.array(image)

        # Convertir la imagen a escala de grises
        imagen_gris = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

        # Aplicar un umbral adaptativo para convertir la imagen en binaria
        _, binary = cv2.threshold(imagen_gris, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

        # Encontrar contornos en la imagen binaria
        contornos, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Seleccionar el contorno más grande (el contorno del sol)
        contorno_sol = max(contornos, key=cv2.contourArea)

        # Obtener el círculo mínimo que encierra el contorno del sol
        (x, y), radio_sol = cv2.minEnclosingCircle(contorno_sol)
        centro_sol = (int(x), int(y))
        radio_sol = int(radio_sol)

        # Aplicar umbralización adaptativa para detectar las manchas solares dentro del disco solar
        binary_manchas_solares = cv2.adaptiveThreshold(imagen_gris, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 55, 53)

        # Encontrar contornos en la imagen binaria de las manchas solares
        contornos_manchas_solares, _ = cv2.findContours(binary_manchas_solares, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Crear una nueva imagen en blanco del mismo tamaño que la original
        imagen_con_circulo = np.zeros_like(image_np)

        # Dibujar el círculo que contiene el contorno del sol en la nueva imagen
        cv2.circle(imagen_con_circulo, centro_sol, radio_sol, (0, 0, 255), 2)

        # Dibujar los contornos de las manchas solares dentro del disco solar en la nueva imagen
        for contorno in contornos_manchas_solares:
            cv2.drawContours(imagen_con_circulo, [contorno], 0, (0, 0, 255), 2)

        # Mostrar la imagen con el círculo que contiene el contorno del sol y los contornos de las manchas solares dentro del disco solar
        st.image(imagen_con_circulo, caption="Imagen con contornos", use_column_width=True)

if __name__ == "__main__":
    main()
