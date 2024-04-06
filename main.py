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
    page = st.sidebar.radio("Seleccionar página", ("Visualizador de Imagen del Sol", "Visualizador de Eclipse", "Reloj","Galeria"))
    
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
            # Agregar deslizadores para controlar los parámetros de borde
            with st.sidebar:
                st.title("Parámetros de borde")
                ksize = st.slider("Tamaño del bloque", 3, 21, 11)
                c = st.slider("C", -10, 10, 2)

            # Aplicar umbralización adaptativa para detectar las manchas solares dentro del disco solar
            binary_manchas_solares = cv2.adaptiveThreshold(imagen_gris, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, kzise, c)

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

            cv2.putText(imagen_con_circulo, f"Autor: {autor}", bottom_left_corner, font, font_scale, font_color, line_type, cv2.LINE_AA)
            cv2.putText(imagen_con_circulo, f"Lugar: {lugar}", (bottom_left_corner[0], bottom_left_corner[1] - 20), font, font_scale, font_color, line_type, cv2.LINE_AA)
            cv2.putText(imagen_con_circulo, f"Hora: {hora}", (bottom_left_corner[0], bottom_left_corner[1] - 40), font, font_scale, font_color, line_type, cv2.LINE_AA)
            cv2.putText(imagen_con_circulo, f"Fecha: {fecha}", (bottom_left_corner[0], bottom_left_corner[1] - 60), font, font_scale, font_color, line_type, cv2.LINE_AA)
             
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
                "Centro_X (pixeles)": [],
                "Centro_Y (pixeles)": [],
                "Tamaño (pix^2)": [],
                "Distancia Radial (pix)": [],
                "Ángulo (grados)": []
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
                    data["Centro_X (pixeles)"].append(cX)
                    data["Centro_Y (pixeles)"].append(cY)
                    data["Tamaño (pix^2)"].append(tamano_contorno)
                    data["Distancia Radial (pix)"].append(distancia_radial)
                    data["Ángulo (grados)"].append(angulo_grados)

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
        #import numpy as np
        import matplotlib.pyplot as plt
        from matplotlib.patches import Circle
        from PIL import Image
        import shapely.geometry as sg
        #import streamlit as st
        
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
                font_scale = 0.8
                font_color = (255, 255, 255)
                line_type = 1

                cv2.putText(image_bgr, f"Autor: {autor}", bottom_left_corner, font, font_scale, font_color, line_type, cv2.LINE_AA)
                cv2.putText(image_bgr, f"Lugar: {lugar}", (bottom_left_corner[0], bottom_left_corner[1] - 30), font, font_scale, font_color, line_type, cv2.LINE_AA)
                cv2.putText(image_bgr, f"Hora: {hora}", (bottom_left_corner[0], bottom_left_corner[1] - 60), font, font_scale, font_color, line_type, cv2.LINE_AA)
                cv2.putText(image_bgr, f"Fecha: {fecha}", (bottom_left_corner[0], bottom_left_corner[1] - 90), font, font_scale, font_color, line_type, cv2.LINE_AA)

                # Convertir la imagen de nuevo a formato compatible con Streamlit
                imagen_with_text = Image.fromarray(cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB))

                st.write("Esta es tu foto del Sol:")
                # Mostrar la imagen con texto
                st.image(imagen_with_text, caption="Fotografía del Sol durante el eclipse", use_column_width=True)



                
        import numpy as np
        import matplotlib.pyplot as plt
        from matplotlib.patches import Circle
        from PIL import Image
        import shapely.geometry as sg
        import streamlit as st

        def update(pos_x1, pos_y1, radio1, pos_x2, pos_y2, radio2, x_limit, y_limit):
            # Crear una nueva figura
            fig, ax = plt.subplots()

            # Establecer el fondo del gráfico a negro
            ax.set_facecolor('black')

            # Cargar la imagen del eclipse parcial del sol (imagen de ejemplo)
            #img = Image.open('eclipse_solar.jpg')  # Ruta de la imagen del eclipse solar
            img = Image.open(uploaded_file)
            ax.imshow(img, extent=[-x_limit, x_limit, -y_limit, y_limit])  # Ajustar límites según los deslizadores

            # Dibujar los círculos con las posiciones y radios proporcionados
            circle1 = Circle((pos_x1, pos_y1), radio1, color='blue', fill=False)
            circle2 = Circle((pos_x2, pos_y2), radio2, color='orange', fill=False)
            ax.add_patch(circle1)
            ax.add_patch(circle2)

            # Calcular el área del círculo naranja
            area_orange_circle = np.pi * radio2**2
            area_blue_circle = np.pi*radio1**2

            # Calcular el área de la intersección de los dos círculos
            circle1_polygon = sg.Point(pos_x1, pos_y1).buffer(radio1)
            circle2_polygon = sg.Point(pos_x2, pos_y2).buffer(radio2)
            intersection_area = circle1_polygon.intersection(circle2_polygon).area

            # Calcular el área dentro del círculo naranja que no está dentro de la intersección con el círculo azul
            area_not_in_intersection = area_orange_circle - intersection_area

            # Calcular el porcentaje del área dentro del círculo naranja que no está dentro de la intersección
            percentage_area_not_in_intersection = (area_not_in_intersection / area_orange_circle) * 100

            # Configurar el gráfico
            ax.axis('equal')
            ax.set_xlim(-x_limit, x_limit)
            ax.set_ylim(-y_limit, y_limit)
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_title('Ajuste la posición y radio de los círculos para que coincidan con su fotografía del eclipse solar')
            ax.grid(True)

            # Mostrar la figura en Streamlit
            st.pyplot(fig)

            # Mostrar los resultados
            st.write(f"Área total del disco solar (en píxeles cuadrados): {area_orange_circle}")
            st.write(f"Área total del contorno lunar (en píxeles cuadrados): {area_blue_circle}")
            st.write(f"Área oculta (en píxeles cuadrados): {intersection_area}")
            st.write(f"Área visible del disco solar (en píxeles cuadrados): {area_not_in_intersection}")
            st.write(f"Porcentaje del área visible del disco solar: {percentage_area_not_in_intersection}%")

        # Crear los controles deslizantes en Streamlit
        #pos_x1 = st.slider('PosX1:', -20.0, 20.0, 0.0, 0.1)
        #pos_y1 = st.slider('PosY1:', -20.0, 20.0, 0.0, 0.1)
        #radio1 = st.slider('Radio1:', 0.0, 20.0, 10.0, 0.1)    
        #pos_x2 = st.slider('PosX2:', -20.0, 20.0, 5.0, 0.1)
        #pos_y2 = st.slider('PosY2:', -20.0, 20.0, 5.0, 0.1)
        #radio2 = st.slider('Radio2:', 0.0, 20.0, 7.0, 0.1)
        #x_limit = st.slider('Límite X:', 1.0, 50.0, 30.0, 1.0)
        #y_limit = st.slider('Límite Y:', 1.0, 50.0, 20.0, 1.0)

        with st.sidebar:
            pos_x1 = st.slider('PosX1', -20.0, 20.0, 0.0, 0.1)
            pos_y1 = st.slider('PosY1', -20.0, 20.0, 0.0, 0.1)
            radio1 = st.slider('Radio1', 0.0, 20.0, 10.0, 0.1)
            pos_x2 = st.slider('PosX2', -20.0, 20.0, 5.0, 0.1)
            pos_y2 = st.slider('PosY2', -20.0, 20.0, 5.0, 0.1)
            radio2 = st.slider('Radio2', 0.0, 20.0, 7.0, 0.1)
            x_limit = st.slider('Límite X', 1.0, 50.0, 30.0, 1.0)
            y_limit = st.slider('Límite Y', 1.0, 50.0, 20.0, 1.0)

        
        # Llamar a la función update con los valores de los deslizadores
        update(pos_x1, pos_y1, radio1, pos_x2, pos_y2, radio2, x_limit, y_limit)

        # Cargar la imagen del eclipse parcial del sol
        def calculate_percentage_area_not_in_intersection(pos_x1, pos_y1, radio1, pos_x2, pos_y2, radio2):
        # Calcular el área del círculo naranja
            area_orange_circle = np.pi * radio2**2

            # Calcular el área de la intersección de los dos círculos
            circle1_polygon = sg.Point(pos_x1, pos_y1).buffer(radio1)
            circle2_polygon = sg.Point(pos_x2, pos_y2).buffer(radio2)
            intersection_area = circle1_polygon.intersection(circle2_polygon).area

            # Calcular el área dentro del círculo naranja que no está dentro de la intersección con el círculo azul
            area_not_in_intersection = area_orange_circle - intersection_area

            # Calcular el porcentaje del área dentro del círculo naranja que no está dentro de la intersección
            percentage_area_not_in_intersection = (area_not_in_intersection / area_orange_circle) * 100

            return percentage_area_not_in_intersection
        # Llamar a la función update con los valores de los deslizadores para obtener percentage_area_not_in_intersection
        percentage_area_not_in_intersection = calculate_percentage_area_not_in_intersection(pos_x1, pos_y1, radio1, pos_x2, pos_y2, radio2)
        percentage_area_not_in_intersection_formatted = "{:.2f}".format(percentage_area_not_in_intersection)

        
        if uploaded_file is not None:
            import cv2
            import numpy as np
            #import numpy as np
            import matplotlib.pyplot as plt
            from matplotlib.patches import Circle
            from PIL import Image
            import shapely.geometry as sg
            image = Image.open(uploaded_file)

            # Convertir la imagen RGB a formato BGR
            image_bgr = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

            # Crear una copia de la imagen para dibujar
            img_with_text = image_bgr.copy()

            # Convertir la imagen a formato OpenCV
            img_cv2 = np.array(img_with_text)

            # Dibujar el texto con la información sobre la imagen
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottom_left_corner = (10, image_bgr.shape[0] - 10)
            font_scale = 0.8
            font_color = (255, 255, 255)
            line_type = 1

            cv2.putText(image_bgr, f"Autor: {autor}", bottom_left_corner, font, font_scale, font_color, line_type, cv2.LINE_AA)
            cv2.putText(image_bgr, f"Lugar: {lugar}", (bottom_left_corner[0], bottom_left_corner[1] - 30), font, font_scale, font_color, line_type, cv2.LINE_AA)
            cv2.putText(image_bgr, f"Hora: {hora}", (bottom_left_corner[0], bottom_left_corner[1] - 60), font, font_scale, font_color, line_type, cv2.LINE_AA)
            cv2.putText(image_bgr, f"Fecha: {fecha}", (bottom_left_corner[0], bottom_left_corner[1] - 90), font, font_scale, font_color, line_type, cv2.LINE_AA)
            cv2.putText(image_bgr, f"Porcentaje visible: {percentage_area_not_in_intersection_formatted}%", (bottom_left_corner[0], bottom_left_corner[1] - 120), font, font_scale, font_color, line_type, cv2.LINE_AA)

            # Convertir la imagen de nuevo a formato compatible con Streamlit
            imagen_with_text = Image.fromarray(cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB))

            st.write("Esta es tu foto del Sol:")
            # Mostrar la imagen con texto
            st.image(imagen_with_text, caption="Fotografía del Sol durante el eclipse", use_column_width=True)


        import cv2
        import streamlit as st
        import numpy as np
        import requests
        from io import BytesIO
        import matplotlib.pyplot as plt

        def calculate_percentage_area_not_in_intersection(pos_x1, pos_y1, radio1, pos_x2, pos_y2, radio2):
        # Calcular el área del círculo naranja
            area_orange_circle = np.pi * radio2**2

            # Calcular el área de la intersección de los dos círculos
            circle1_polygon = sg.Point(pos_x1, pos_y1).buffer(radio1)
            circle2_polygon = sg.Point(pos_x2, pos_y2).buffer(radio2)
            intersection_area = circle1_polygon.intersection(circle2_polygon).area

            # Calcular el área dentro del círculo naranja que no está dentro de la intersección con el círculo azul
            area_not_in_intersection = area_orange_circle - intersection_area

            # Calcular el porcentaje del área dentro del círculo naranja que no está dentro de la intersección
            percentage_area_not_in_intersection = (area_not_in_intersection / area_orange_circle) * 100

            return percentage_area_not_in_intersection
        percentage_area_not_in_intersection = calculate_percentage_area_not_in_intersection(pos_x1, pos_y1, radio1, pos_x2, pos_y2, radio2)
        #percentage_area_not_in_intersection_formatted = "{:.2f}".format(percentage_area_not_in_intersection)
        
        # Función para disminuir el brillo de una imagen manteniendo el formato RGB
        def decrease_brightness(image, adjustment):
            # Convertir la imagen a escala de grises
            gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
            # Aplicar el ajuste de brillo
            adjusted_gray_image = np.clip(gray_image.astype(np.float32) - adjustment, 0, 255).astype(np.uint8)
            # Convertir la imagen ajustada de nuevo a RGB manteniendo el canal de luminancia (Y) original
            yuv_image = cv2.cvtColor(image, cv2.COLOR_RGB2YUV)
            yuv_image[:, :, 0] = adjusted_gray_image
            adjusted_image_rgb = cv2.cvtColor(yuv_image, cv2.COLOR_YUV2RGB)
            return adjusted_image_rgb

        # URL de la imagen en tu repositorio de GitHub
        url = 'https://raw.githubusercontent.com/SArcD/SolarSpot/main/paisaje.jpg'

        # Obtener la imagen desde la URL
        response = requests.get(url)

        # Verificar si la respuesta es válida
        if response.status_code == 200:
            # Convertir los datos de la respuesta a una matriz numpy que OpenCV pueda entender
            image_bytes = BytesIO(response.content)
            image_np = np.asarray(bytearray(image_bytes.read()), dtype="uint8")
    
            # Decodificar la imagen con los canales de color RGB
            image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
    
            # Convertir el orden de los canales de color de BGR a RGB
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Verificar si la imagen se cargó correctamente
            if image_rgb is not None:
                # Calcular el ajuste de brillo en función de percentage_area_not_in_intersection_formatted
                #percentage_area_not_in_intersection_formatted = 10.00  # Ejemplo de valor con dos decimales
        
                # Escalar el ajuste de brillo al rango [-100, 100]
                #brightness_adjustment = int((percentage_area_not_in_intersection_formatted - 50.0) * 2.0)
                brightness_adjustment = int((50.0 - percentage_area_not_in_intersection) * 2.0)
                
                # Aplicar el ajuste de brillo a la imagen
                brightened_image = decrease_brightness(image_rgb, brightness_adjustment)
        
                # Crear una figura con dos subtramas
                fig, axes = plt.subplots(1, 2, figsize=(12, 6))
        
                # Mostrar la imagen original en la primera subtrama
                axes[0].imshow(image_rgb)
                axes[0].set_title('Condiciones de luz (día despejado)')
                axes[0].axis('off')
        
                # Mostrar la imagen con el brillo disminuido en la segunda subtrama
                axes[1].imshow(brightened_image)
                axes[1].set_title('Condiciones de luz durante el eclipse')
                axes[1].axis('off')
        
                # Ajustar el diseño y mostrar la figura en Streamlit
                st.pyplot(fig)
            else:
                st.write("No se pudo cargar la imagen desde la URL proporcionada.")
        else:
            st.write("Error al obtener la imagen desde la URL.")

    elif page == "Reloj":

        import streamlit as st        
        import pandas as pd
        from datetime import datetime
        import pytz

        # Lista de ciudades con su correspondiente zona horaria
        cities = {
            "New York": "America/New_York",
            "London": "Europe/London",
            "Tokyo": "Asia/Tokyo",
            "Sydney": "Australia/Sydney",
            "Ciudad de México": "America/Mexico_City",
            "Colima (Colima, México)": "America/Mexico_City",
            "Morelia (Michoacán, México)": "America/Mexico_City",
            "Zacatecas (Zacatecas, México)": "America/Mexico_City",
            "Ensenada (Baja California)": "America/Tijuana"
        }

        # Obtener la fecha y hora actual para cada ciudad    
        current_times = {city: datetime.now(pytz.timezone(timezone)) for city, timezone in cities.items()}

        # Crear un DataFrame con los horarios de las ciudades
        df = pd.DataFrame(current_times.items(), columns=["Ciudad", "Fecha/Hora local"])

        # Separar la fecha y la hora en columnas separadas
        df["Fecha"] = [d.date() for d in df["Fecha/Hora local"]]
        df["Hora"] = [d.time() for d in df["Fecha/Hora local"]]
        df.drop(columns=["Fecha/Hora local"], inplace=True)

        st.write("### Horarios de las ciudades")
        st.write(df)

        import streamlit as st
        from streamlit_folium import folium_static
        import folium
        
        # Crear un mapa centrado en México
        mexico_map = folium.Map(location=[23.6345, -102.5528], zoom_start=5)
        # Agregar un marcador en la Ciudad de México
        folium.Marker([19.4326, -99.1332], popup='Ciudad de México').add_to(mexico_map)
        # Agregar un marcador en Guadalajara
        folium.Marker([20.6597, -103.3496], popup='Guadalajara').add_to(mexico_map)
        # Agregar un marcador en Monterrey
        folium.Marker([25.6866, -100.3161], popup='Monterrey').add_to(mexico_map)
        # Agregar un marcador en Colima, Colima, México
        folium.Marker([19.2493, -103.7271], popup='Colima, Colima, México').add_to(mexico_map)
        # Agregar un marcador en Zacatecas, Zacatecas, México
        folium.Marker([22.7709, -102.5832], popup='Zacatecas, Zacatecas, México').add_to(mexico_map)
        # Agregar un marcador en Morelia, Michoacán, México
        folium.Marker([19.4326, -101.897], popup='Morelia, Michoacán, México').add_to(mexico_map)
        # Agregar un marcador en Querétaro, Querétaro, México
        folium.Marker([20.5881, -100.3881], popup='Querétaro, Querétaro, México').add_to(mexico_map)
        # Agregar un marcador en Ensenada, Baja California, México
        folium.Marker([31.8661, -116.5964], popup='Ensenada, Baja California, México').add_to(mexico_map)
        # Agregar un marcador en Toronto, Ontario, Canadá
        folium.Marker([43.65107, -79.347015], popup='Toronto, Ontario, Canadá').add_to(mexico_map)
        # Agregar un marcador en Quito, Ecuador
        folium.Marker([-0.1905, -78.4835], popup='Quito, Ecuador').add_to(mexico_map)
        # Agregar un marcador en Santiago de Chile, Chile
        folium.Marker([-33.4372, -70.6506], popup='Santiago de Chile, Chile').add_to(mexico_map)


        # Mostrar el mapa en Streamlit
        folium_static(mexico_map)


        import streamlit as st
        from streamlit_folium import folium_static
        import folium
        from geopy.distance import geodesic

        # Diccionario con las coordenadas de las ciudades
        cities = {
            "Ciudad de México": [19.4326, -99.1332],
            "Guadalajara": [20.6597, -103.3496],
            "Monterrey": [25.6866, -100.3161],
            "Colima, Colima, México": [19.2493, -103.7271],
            "Zacatecas, Zacatecas, México": [22.7709, -102.5832],
            "Morelia, Michoacán, México": [19.4326, -101.897],
            "Querétaro, Querétaro, México": [20.5881, -100.3881],
            "Ensenada, Baja California, México": [31.8661, -116.5964],
            "Santiago de Chile, Chile": [-33.4372, -70.6506],
            "Quito, Ecuador": [-0.1905, -78.4835],
            "Ontario, Canadá": [43.65107, -79.347015]
        }

        # Obtener nombres de ciudades
        city_names = list(cities.keys())

        # Crear elementos de selección para elegir las ciudades
        city1 = st.selectbox("Selecciona la primera ciudad:", city_names)
        city2 = st.selectbox("Selecciona la segunda ciudad:", city_names)

        # Función para calcular la distancia entre dos ciudades
        def calculate_distance(city1, city2):
            coord1 = cities[city1]
            coord2 = cities[city2]
            distance = geodesic(coord1, coord2).kilometers
            return distance

        # Calcular la distancia entre las ciudades seleccionadas
        distance = calculate_distance(city1, city2)

        # Mostrar la distancia en la interfaz
        st.write(f"La distancia entre {city1} y {city2} es de {distance:.2f} kilómetros.")

    if page == "Galeria":
        import streamlit as st

        # URLs de las imágenes en el repositorio de GitHub
        images_with_names = [
            ("https://raw.githubusercontent.com/SArcD/SolarSpot/7713e5032a73af20a00f993a988ed93c794f2161/fotos/29032024_gs.jpg", "29032024_gs.jpg"),
            ("https://raw.githubusercontent.com/SArcD/SolarSpot/7713e5032a73af20a00f993a988ed93c794f2161/fotos/28032024_gs.jpg", "28032024_gs.jpg"),
            ("https://raw.githubusercontent.com/SArcD/SolarSpot/7713e5032a73af20a00f993a988ed93c794f2161/fotos/27032024_gs.jpg", "27032024_gs.jpg"),
            ("https://raw.githubusercontent.com/SArcD/SolarSpot/7713e5032a73af20a00f993a988ed93c794f2161/fotos/26032024_gs.jpg", "26032024_gs.jpg"),
            ("https://raw.githubusercontent.com/SArcD/SolarSpot/7713e5032a73af20a00f993a988ed93c794f2161/fotos/25032024_gs.jpg", "25032024_gs.jpg"),
            ("https://raw.githubusercontent.com/SArcD/SolarSpot/7713e5032a73af20a00f993a988ed93c794f2161/fotos/24032024_gs.jpg", "24032024_gs.jpg"),
            ("https://raw.githubusercontent.com/SArcD/SolarSpot/7713e5032a73af20a00f993a988ed93c794f2161/fotos/23032024_gs.jpg", "23032024_gs.jpg"),
            ("https://raw.githubusercontent.com/SArcD/SolarSpot/7713e5032a73af20a00f993a988ed93c794f2161/fotos/21032024_gs.jpg", "21032024_gs.jpg"),
            ("https://raw.githubusercontent.com/SArcD/SolarSpot/7713e5032a73af20a00f993a988ed93c794f2161/fotos/19032024_gs.jpg", "19032024_gs.jpg"),            
        ]

        # Número de columnas en la matriz
        num_columns = 3

        # Calcula el número de filas basado en el número de imágenes y columnas
        num_rows = -(-len(images_with_names) // num_columns)

        # Crea una cuadrícula de imágenes con sus nombres
        for i in range(num_rows):
            col1, col2, col3 = st.columns(3)  # Creamos 3 columnas por cada fila
            if i * num_columns < len(images_with_names):
                col1.image(images_with_names[i * num_columns][0], caption=images_with_names[i * num_columns][1], width=200)
            if i * num_columns + 1 < len(images_with_names):
                col2.image(images_with_names[i * num_columns + 1][0], caption=images_with_names[i * num_columns + 1][1], width=200)
            if i * num_columns + 2 < len(images_with_names):
                col3.image(images_with_names[i * num_columns + 2][0], caption=images_with_names[i * num_columns + 2][1], width=200)









    


if __name__ == "__main__":
    main()
