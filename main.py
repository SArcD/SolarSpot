# -*- coding: utf-8 -*-

import streamlit as st
from PIL import Image
import numpy as np
import cv2

def main():
    st.title("Visualizador de Imagen del Sol")
    st.write("Carga una imagen del sol y mírala aquí! (formatos posibles: .jpg, jpeg., .png)")

    uploaded_file = st.file_uploader("Cargar imagen", type=["jpg", "jpeg", "png"])
    st.write("Escribe tus datos sobre la imagen (evita el uso de acento)")

    if uploaded_file is not None:
        # Mostrar la imagen cargada
        image = Image.open(uploaded_file)
        
        # Cajas de entrada para el autor, lugar y hora
        autor = st.text_input("Autor", "")
        lugar = st.text_input("Lugar", "")
        hora = st.text_input("Hora", "")

        if st.button("Mostrar datos en imagen"):
            # Convertir la imagen cargada a una matriz numpy
            image_np = np.array(image)

            # Dibujar texto en la imagen
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottom_left_corner = (10, image_np.shape[0] - 10)
            font_scale = 0.5
            font_color = (255, 255, 255)
            line_type = 1

            #cv2.putText(image_np, f"Autor: {autor}", bottom_left_corner, font, font_scale, font_color, line_type)
            #cv2.putText(image_np, f"Lugar: {lugar}", (bottom_left_corner[0], bottom_left_corner[1] - 20), font, font_scale, font_color, line_type)
            #cv2.putText(image_np, f"Hora: {hora}", (bottom_left_corner[0], bottom_left_corner[1] - 40), font, font_scale, font_color, line_type)
            cv2.putText(image_np, f"Autor: {autor}", bottom_left_corner, font, font_scale, font_color, line_type, cv2.LINE_AA)
            cv2.putText(image_np, f"Lugar: {lugar}", (bottom_left_corner[0], bottom_left_corner[1] - 20), font, font_scale, font_color, line_type, cv2.LINE_AA)
            cv2.putText(image_np, f"Hora: {hora}", (bottom_left_corner[0], bottom_left_corner[1] - 40), font, font_scale, font_color, line_type, cv2.LINE_AA)
            cv2.putText(image_np, f"Fecha: {fecha}", (bottom_left_corner[0], bottom_left_corner[1] - 60), font, font_scale, font_color, line_type, cv2.LINE_AA)


            
            # Convertir la imagen de nuevo a formato compatible con Streamlit
            image_with_text = Image.fromarray(image_np)
            st.write("Esta es tu foto del Sol:")
            # Mostrar la imagen con texto
            st.image(image_with_text, caption="Fotografía del Sol", use_column_width=True)


    
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


        # Dibujar los contornos de las manchas solares dentro del disco solar en la nueva imagen
        for i, contorno in enumerate(contornos_manchas_solares, start=1):
            # Dibujar el contorno
            cv2.drawContours(imagen_con_circulo, [contorno], 0, (0, 0, 255), 2)

            # Calcular el centro del contorno
            M = cv2.moments(contorno)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
            else:
                cX, cY = 0, 0

            # Etiquetar el contorno con un número sin superposiciones
            etiqueta = str(i)
            (etiqueta_ancho, etiqueta_alto), _ = cv2.getTextSize(etiqueta, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)
            cv2.putText(imagen_con_circulo, etiqueta, (cX - etiqueta_ancho // 2, cY + etiqueta_alto // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        # Mostrar la imagen con el círculo que contiene el contorno del sol y los contornos de las manchas solares dentro del disco solar
        st.image(imagen_con_circulo)
if __name__ == "__main__":
    main()
