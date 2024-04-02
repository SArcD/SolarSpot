# -*- coding: utf-8 -*-

import streamlit as st
from PIL import Image
import numpy as np
import cv2
import pandas as pd
import math
import cv2


def main():
    import streamlit as st
    import cv2
    import numpy as np
    from PIL import Image
    # Crear una barra lateral para la navegación entre páginas
    page = st.sidebar.radio("Seleccionar página", ("Visualizador de Imagen del Sol", "Visualizador de Eclipse"))
    
    if page == "Visualizador de Imagen del Sol":
        import streamlit as st
        import cv2
        import numpy as np
        from PIL import Image

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
            fecha = st.text_input("Fecha","")

            if st.button("Mostrar datos en imagen"):
                # Convertir la imagen cargada a una matriz numpy
                image_np = np.array(image)

                # Dibujar texto en la imagen
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottom_left_corner = (10, image_np.shape[0] - 10)
                font_scale = 0.5
                font_color = (255, 255, 255)
                line_type = 1

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
            # Mostrar la imagen con el círculo que contiene el contorno del sol y los contornos de las manchas solares dentro del disco solar
                # Dibujar los contornos de las manchas solares dentro del disco solar en la nueva imagen
            for contorno in contornos_manchas_solares:
                # Calcular el centro del contorno
                M = cv2.moments(contorno)
                if M["m00"] != 0:
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                else:
                    cX, cY = 0, 0

                # Calcular la distancia desde el centro del contorno del sol al centro del contorno actual
                distancia_centros = math.sqrt((centro_sol[0] - cX)**2 + (centro_sol[1] - cY)**2)

                # Si la distancia es menor o igual a 1.1 veces el radio del sol, dibuja el contorno
                if distancia_centros <= 1.1 * radio_sol:
                    # Dibujar el contorno
                    cv2.drawContours(imagen_con_circulo, [contorno], 0, (0, 0, 255), 2)
                    #st.image(imagen_con_circulo, caption="Imagen con contornos", use_column_width=True)

                # Mapear la etiqueta original a la nueva etiqueta y actualizar el diccionario
                #etiquetas_renombradas[len(etiquetas_renombradas) + 1] = nueva_etiqueta

                # Etiquetar el contorno con la nueva etiqueta
                #(etiqueta_ancho, etiqueta_alto), _ = cv2.getTextSize(str(nueva_etiqueta), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)
                #cv2.putText(imagen_con_circulo, str(nueva_etiqueta), (cX - etiqueta_ancho // 2, cY + etiqueta_alto // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

                # Incrementar la nueva etiqueta
                #nueva_etiqueta += 1

        
            cv2.putText(imagen_con_circulo, f"Autor: {autor}", bottom_left_corner, font, font_scale, font_color, line_type, cv2.LINE_AA)
            cv2.putText(imagen_con_circulo, f"Lugar: {lugar}", (bottom_left_corner[0], bottom_left_corner[1] - 20), font, font_scale, font_color, line_type, cv2.LINE_AA)
            cv2.putText(imagen_con_circulo, f"Hora: {hora}", (bottom_left_corner[0], bottom_left_corner[1] - 40), font, font_scale, font_color, line_type, cv2.LINE_AA)
            cv2.putText(imagen_con_circulo, f"Fecha: {fecha}", (bottom_left_corner[0], bottom_left_corner[1] - 60), font, font_scale, font_color, line_type, cv2.LINE_AA)
                   
            st.image(imagen_con_circulo, caption="Imagen con contornos", use_column_width=True)

            # Diccionario para mapear las etiquetas originales a las etiquetas renombradas
            etiquetas_renombradas = {}

            # Contador para llevar el seguimiento de la etiqueta renombrada
            nueva_etiqueta = 1

            # Dibujar los contornos de las manchas solares dentro del disco solar en la nueva imagen
            for contorno in contornos_manchas_solares:
                # Calcular el centro del contorno
                M = cv2.moments(contorno)
                if M["m00"] != 0:
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                else:
                    cX, cY = 0, 0

                # Calcular la distancia desde el centro del contorno del sol al centro del contorno actual
                distancia_centros = math.sqrt((centro_sol[0] - cX)**2 + (centro_sol[1] - cY)**2)

                # Si la distancia es menor o igual a 1.1 veces el radio del sol, dibuja el contorno
                if distancia_centros <= 1.1 * radio_sol:
                    # Dibujar el contorno
                    cv2.drawContours(imagen_con_circulo, [contorno], 0, (0, 0, 255), 2)
                    #st.image(imagen_con_circulo, caption="Imagen con contornos", use_column_width=True)

                    # Mapear la etiqueta original a la nueva etiqueta y actualizar el diccionario
                    etiquetas_renombradas[len(etiquetas_renombradas) + 1] = nueva_etiqueta

                    # Etiquetar el contorno con la nueva etiqueta
                    (etiqueta_ancho, etiqueta_alto), _ = cv2.getTextSize(str(nueva_etiqueta), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)
                    cv2.putText(imagen_con_circulo, str(nueva_etiqueta), (cX - etiqueta_ancho // 2, cY + etiqueta_alto // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

                    # Incrementar la nueva etiqueta
                    nueva_etiqueta += 1

            # Mostrar la imagen con el círculo que contiene el contorno del sol y los contornos de las manchas solares dentro del disco solar
            
            st.image(imagen_con_circulo, caption="Imagen con contornos contabilizados", use_column_width=True)



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

            # Crear un DataFrame para almacenar la información de los contornos
            data = {
                "Contorno": [],
                "Centro_X": [],
                "Centro_Y": [],
                "Tamaño (píxeles)": [],
                "Distancia Radial": [],
                "Ángulo (radianes)": []
            }

            # Contador para llevar el seguimiento de la etiqueta renombrada
            nueva_etiqueta = 1

            #     Dibujar los contornos de las manchas solares dentro del disco solar en la nueva imagen
            for i, contorno in enumerate(contornos_manchas_solares, start=1):
                # Calcular el centro del contorno
                M = cv2.moments(contorno)
                if M["m00"] != 0:
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                else:
                    cX, cY = 0, 0

                # Calcular el área del contorno
                area = cv2.contourArea(contorno)

                # Calcular la distancia desde el centro del contorno del sol al centro del contorno actual
                distancia_centros = math.sqrt((centro_sol[0] - cX)**2 + (centro_sol[1] - cY)**2)

                # Si la distancia es menor o igual a 1.1 veces el radio del sol, procede
                if distancia_centros <= 1.1 * radio_sol and area > 0:
                    # Dibujar el contorno
                    cv2.drawContours(imagen_con_circulo, [contorno], 0, (0, 0, 255), 2)

                    # Calcular el tamaño del contorno en píxeles
                    tamano_contorno = math.sqrt(area / math.pi)

                    # Calcular las coordenadas polares del centro del contorno
                    distancia_radial = math.sqrt((cX - centro_sol[0])**2 + (cY - centro_sol[1])**2)
                    angulo = math.atan2(cY - centro_sol[1], cX - centro_sol[0])
                    angulo_grados = math.degrees(angulo)

                    # Agregar los valores al DataFrame
                    data["Contorno"].append(nueva_etiqueta)
                    data["Centro_X"].append(cX)
                    data["Centro_Y"].append(cY)
                    data["Tamaño (píxeles)"].append(tamano_contorno)
                    data["Distancia Radial"].append(distancia_radial)
                    data["Ángulo (radianes)"].append(angulo_grados)

                    # Incrementar la nueva etiqueta
                    nueva_etiqueta += 1
     
            # Convertir el diccionario de datos a DataFrame
            df = pd.DataFrame(data)

            # Mostrar el DataFrame
            st.write("Información de los contornos:")
            st.write(df)


    elif page == "Visualizador de Eclipse":
        import cv2
        import numpy as np
        st.title("Visualizador de Eclipse")
        st.write("Esta es la página del visualizador de eclipse. Aquí puedes agregar el código para visualizar eclipses.")

        st.write("Carga una imagen del sol y mírala aquí! (formatos posibles: .jpg, jpeg., .png)")

        uploaded_file = st.file_uploader("Cargar imagen", type=["jpg", "jpeg", "png"])
        st.write("Escribe tus datos sobre la imagen (evita el uso de acento)")

        if uploaded_file is not None:
            # Mostrar la imagen cargada
            image = Image.open(uploaded_file)
        
            # Convertir la imagen RGB a formato BGR
            image_bgr = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

            # Cajas de entrada para el autor, lugar y hora
            autor = st.text_input("Autor", "")
            lugar = st.text_input("Lugar", "")
            hora = st.text_input("Hora", "")
            fecha = st.text_input("Fecha","")

            if st.button("Mostrar datos en imagen"):
                # Convertir la imagen cargada a una matriz numpy
                image_np = np.array(image)

                # Dibujar texto en la imagen
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottom_left_corner = (10, image_np.shape[0] - 10)
                font_scale = 0.5
                font_color = (255, 255, 255)
                line_type = 1

                cv2.putText(image_bgr, f"Autor: {autor}", bottom_left_corner, font, font_scale, font_color, line_type, cv2.LINE_AA)
                cv2.putText(image_bgr, f"Lugar: {lugar}", (bottom_left_corner[0], bottom_left_corner[1] - 20), font, font_scale, font_color, line_type, cv2.LINE_AA)
                cv2.putText(image_bgr, f"Hora: {hora}", (bottom_left_corner[0], bottom_left_corner[1] - 40), font, font_scale, font_color, line_type, cv2.LINE_AA)
                cv2.putText(image_bgr, f"Fecha: {fecha}", (bottom_left_corner[0], bottom_left_corner[1] - 60), font, font_scale, font_color, line_type, cv2.LINE_AA)

                # Convertir la imagen de nuevo a formato compatible con Streamlit
                imagen_with_text = Image.fromarray(cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB))

                st.write("Esta es tu foto del Sol:")
                # Mostrar la imagen con texto
                st.image(imagen_with_text, caption="Fotografía del Sol durante el eclipse", use_column_width=True)


                def detectar_disco_solar(imagen):
                    
                    # Convertir la imagen a escala de grises
                    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

                    # Aplicar umbral adaptativo con parámetros ajustados
                    thresh = cv2.adaptiveThreshold(imagen_gris, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 15, 10)

                    # Encontrar contornos en la imagen umbralizada
                
                    contornos, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                    # Seleccionar el contorno más grande (el disco solar)
                    contorno_disco_solar = max(contornos, key=cv2.contourArea)

                    # Encontrar el círculo que encierra el contorno
                    (x, y), radio = cv2.minEnclosingCircle(contorno_disco_solar)
                    centro_x = int(x)
                    centro_y = int(y)
                    
                    return contorno_disco_solar

                
                # Cargar la imagen desde el archivo cargado
                image = Image.open(uploaded_file)
                #    Convertir la imagen RGB a formato BGR
                image_bgr = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                # Detectar el disco solar en la imagen
                contorno_disco_solar = detectar_disco_solar(image_bgr)
                # Dibujar el contorno del disco solar en la imagen
                cv2.drawContours(image_bgr, [contorno_disco_solar], -1, (0, 255, 0), 2)
                # Convertir la imagen de nuevo a formato compatible con Streamlit
                image_with_text = Image.fromarray(cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB))
                #st.write("Esta es tu foto del Sol:")
                # Mostrar la imagen con texto y contorno del disco solar
                st.image(image_with_text, caption="Fotografía del Sol durante el eclipse con el contorno resaltado", use_column_width=True)
                



if __name__ == "__main__":
    main()
