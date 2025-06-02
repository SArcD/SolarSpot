#  Este es el codigo para la visualización de imagenes solares "solar spot"

import streamlit as st #se encarga de generar la aplicaicón interactiva a partir del codigo de python
from PIL import Image  # Se utiliza para cargar y procesar imagenes.
import numpy as np  # realiza  operaciones numéricas
import cv2  # sirve para procesamiento de imagenes
import pandas as pd # genera tablas
import math # carga funciones matematicas 
import cv2


def main():
    import streamlit as st
    import cv2
    import numpy as np
    from PIL import Image
   # Encabezado con logo a la izquierda y título a la derecha
    col1, col2 = st.columns([2, 5])  # Ajusta la proporción si deseas que el título ocupe más espacio
    with col1:
        st.image("Logo.jpg", width=250)  # Tamaño pequeño
    with col2:
        st.markdown("<h1 style='margin-top: 15px;'>Contador de manchas solares</h1>", unsafe_allow_html=True)

    
    # Crear una barra lateral para la navegación entre páginas
    page = st.sidebar.radio("Seleccionar página", ("Las estrellas", "El Sol", "Visualizador de Imagen del Sol", "Visualizador de Eclipse", "Reloj","Galeria"))

    if page == "Las estrellas":
        import streamlit as st
        #from introduccion_estrellas import mostrar_introduccion_estrellas


        #def mostrar_introduccion_estrellas():
        st.title("¿Qué son las estrellas?")
          
        st.markdown("""
        Las **estrellas** son enormes esferas de gas caliente, compuestas principalmente por **hidrógeno** y **helio**.  
        En su núcleo ocurre un proceso llamado **fusión nuclear**, donde los átomos de hidrógeno se combinan para formar helio, liberando **energía** en forma de luz y calor. La estrella mas cercana a nuestro planeta es el Sol, ubicado a una unidad astronómica de distancia (**150 millones de kilómetros**). **Cada segundo el Sol produce \n$$3.86 \\times 10^{26}\\ \\text{watts}$$, lo que equivale a 20 millones de veces el consumo anual de energía en todo el planeta**. Esta energía es la que permite que podamos observar a las estrellas aún a distancias astronómicas.

        """)

        imagen = Image.open("Sol.PNG")
        st.image(imagen, caption="Fotografía del Sol, visto a través de un filtro de luz blanca", use_container_width=True)

        
        st.markdown(
            """
        
        ### 🔭 ¿Cómo las vemos?

        Desde la Tierra, las estrellas aparecen como puntos brillantes en el cielo nocturno.  Aunque están a **años luz** de distancia, su brillo es tan intenso que muchas se pueden ver sin telescopio. Una de las primeras cosas que podemos notar es que existen estrellas con diferentes colores, que van del rojo al azul, a estos colores se les llama **Clases espectrales** y se puede asociar al tamaño, temperatura y masa de cada estrella.
        """)
        # Mostrar imagen ilustrativa
        imagen = Image.open("im_01.png")
        st.image(imagen, caption="Clasificación visual de estrellas por color y temperatura", use_container_width=True)

        st.markdown(
        """
        | Clase espectral ([Wikipedia](https://es.wikipedia.org/wiki/Clasificaci%C3%B3n_estelar)) | Color           | Temperatura aprox. | Ejemplo (clic en el nombre)                         |
        |--------------------------------------------------------|-------------------|---------------------|-----------------------------------------------------|
        | [O](https://wiki.ed-board.net/es/stellar/O)             | 🔵 Azul violáceo  | > 30,000 °C         | [Zeta Puppis](https://es.wikipedia.org/wiki/Zeta_Puppis) |
        | [B](https://wiki.ed-board.net/es/stellar/B)             | 🔵 Azul            | ~10,000–30,000 °C   | [Rigel](https://es.wikipedia.org/wiki/Rigel)        |
        | [A](https://wiki.ed-board.net/es/stellar/A)             | ⚪ Blanco-azulado  | ~7,500–10,000 °C    | [Sirius](https://es.wikipedia.org/wiki/Sirio)       |
        | [F](https://wiki.ed-board.net/es/stellar/F)             | ⚪ Blanco amarillento | ~6,000–7,500 °C | [Procyon](https://es.wikipedia.org/wiki/Procyon)    |
        | [G](https://wiki.ed-board.net/es/stellar/G)             | 🟡 Amarillo        | ~5,200–6,000 °C     | [El Sol](https://es.wikipedia.org/wiki/Sol)         |
        | [K](https://wiki.ed-board.net/es/stellar/K)             | 🟠 Naranja         | ~3,700–5,200 °C     | [Arcturus](https://es.wikipedia.org/wiki/Arcturus)  |
        | [M (gigante)](https://es.wikipedia.org/wiki/Gigante_roja)   | 🔴 Rojo anaranjado | ~3,000–3,700 °C | [Betelgeuse](https://es.wikipedia.org/wiki/Betelgeuse) |
        | [M (enana)](https://wiki.ed-board.net/es/stellar/M)     | 🔴 Rojo tenue      | ~2,400–3,700 °C     | [Proxima Centauri](https://es.wikipedia.org/wiki/Proxima_Centauri) |

        ---
        """)


        ### 🌟 Ciclo de vida estelar

    #    st.markdown("""
    #    Las estrellas **no tienen un único destino**. Su **masa inicial** determina la ruta que seguirán desde su nacimiento hasta su muerte:

    #    1. 🌌 **Nacimiento**: en **nebulosas**, grandes nubes de gas y polvo.
    #    2. 🔥 **Fase principal**: se estabilizan y fusionan hidrógeno en helio durante millones a miles de millones de años.
    #    3. 🌠 **Evolución**: según su masa, pueden transformarse en:
    #       - ⭐ Estrellas como el Sol → se expanden como **gigantes rojas** y terminan como **enanas blancas**.
    #       - 💥 Estrellas masivas → se convierten en **supergigantes**, explotan como **supernovas** y dejan:
    #         - ⚛️ **Estrella de neutrones** (si la masa es intermedia)
    #         - 🕳️ **Agujero negro** (si la masa es muy alta)

    #    ---

    #    """)


        st.markdown("## 🌟 Formación de estrellas en nubes moleculares")

        st.markdown("""
        Las **estrellas nacen dentro de nubes moleculares frías y densas**, compuestas principalmente por **hidrógeno molecular (H₂)**, polvo y otros gases.  
        Estas regiones también son conocidas como **viveros estelares**.

        Cuando una región de la nube alcanza suficiente densidad, comienza a **colapsar por efecto de su propia gravedad**. Este proceso puede ser desencadenado por eventos externos como:
        - Ondas de choque de una supernova cercana
        - Colisiones entre nubes
        - Interacción con brazos espirales galácticos

        Durante el colapso:
        - Se forman zonas **más densas y calientes** llamadas **núcleos preestelares**
        - La materia cae hacia el centro, aumentando la presión y temperatura
        - Surge una **protoestrella**, rodeada de un disco de gas y polvo


        """)

        
        col1, col2 = st.columns(2)

        with col1:
            #st.markdown("#### Nube A")
            with open("Nube_a.gif", "rb") as gif_a:
                gif_bytes_a = gif_a.read()
            st.image(gif_bytes_a, caption="Colapso de una nube molecular", use_container_width=True)

        with col2:
            #st.markdown("#### Nube B")
            with open("nube_b.gif", "rb") as gif_b:
                gif_bytes_b = gif_b.read()
            st.image(gif_bytes_b, caption="Zoom: región densa que dará origen a una protoestrella", use_container_width=True)


        st.markdown(
            """Si la presión y temperatura del centro son suficientes, se inicia la **fusión nuclear**: ¡nace una estrella!

        """)


        st.markdown("## ¿Qué pasa con las estrellas después de formarse?")

        st.markdown("""
        El **Diagrama de Hertzsprung-Russell (HR)** es una herramienta fundamental en astrofísica para **clasificar las estrellas** y entender su **evolución**.

        En este gráfico se relacionan dos propiedades físicas clave:

        - 🔥 **Temperatura efectiva** (en el eje X): de **mayor a menor** hacia la derecha  
        - 💡 **Luminosidad** (en el eje Y): desde **menos luminosa** abajo hasta **más luminosa** arriba


        Las estrellas **no permanecen estáticas** en el diagrama. A lo largo de su vida, **se mueven de una región a otra** dependiendo de su masa y del estado de su núcleo:

        - El Sol, por ejemplo, **nace y vive en la secuencia principal**, pero eventualmente **se moverá hacia la región de las gigantes rojas** y terminará como **una enana blanca**.

        """)


        
        # Mostrar imagen ilustrativa
        imagen = Image.open("im_02.png")
        st.image(imagen, caption="Recorrido evolutivo que siguen estrellas como el sol a lo largo de su vida", use_container_width=True)

        st.markdown(
        """


        - 🌞 La mayoría de las estrellas, incluyendo al Sol, se encuentran en una banda llamada **secuencia principal**.  
        - 🔴 Las **gigantes rojas** y **supergigantes** son frías pero muy luminosas (arriba a la derecha).
        - ⚪ Las **enanas blancas** son muy calientes pero poco luminosas (abajo a la izquierda).

        ---
        """)

        
        st.markdown("### ¿Cómo se ven los cambios?")

        st.markdown(
        """
        La evolución estelar implica cambios bastante notorios en la apariencia, tamaño y brillo de las estrellas. El siguiente video muestra la evolución del Sol desde su nacimiento hasta que se convierte en una gigante roja.
        """)
        
        with open("evo_sol.mp4", "rb") as video_file:
            video_bytes = video_file.read()

        st.video(video_bytes)


    if page == "El Sol":

        
        #### ☀️ ¿Y el Sol?
        #st.markdown(
        #"""

        #Por eso lo vemos tan grande y brillante.  
        #Es una **estrella amarilla de tamaño medio**, pero es fundamental para la vida en la Tierra.
    
        #---

        ### 💡 ¿Sabías que...?

        #- Una cucharadita de una estrella de neutrones pesa millones de toneladas.
        #- Las estrellas parecen "parpadear" por la atmósfera terrestre, no porque realmente lo hagan.
        #- El Sol tiene unos **4,600 millones de años** y vivirá unos 5,000 millones más.

        #---
        #""")

        st.title("☀️ El Sol: Nuestra estrella más cercana")

        st.markdown("""
        El **Sol es una estrella**: una esfera de gas caliente en fusión, **mucho más cerca** de nosotros que las demás estrellas.  El **Sol** es la fuente principal de luz, calor y energía que permite la vida en la Tierra.  
        A continuación, exploraremos sus características, composición, estructura e historia en el universo.

        ---

        ## 🧪 Composición del Sol

        El Sol está formado principalmente por:

        - **Hidrógeno (≈ 74%)**
        - **Helio (≈ 24%)**
        - Pequeñas cantidades de oxígeno, carbono, hierro y otros elementos (≈ 2%)

        La **fusión nuclear** en su núcleo convierte hidrógeno en helio, liberando enormes cantidades de energía.

        📌 Esta energía tarda **miles de años** en llegar desde el núcleo hasta la superficie del Sol, y solo **8 minutos** desde allí hasta la Tierra.

        """)

        # Mostrar imagen ilustrativa
        imagen = Image.open("im_03.png")
        st.image(imagen, caption="Elementos químicos mas abundantes en el Sol", use_container_width=True)


        
        #st.markdown("""
        #---

        ### 🕰️ Historia del Sol
    
        #- 🌌 El Sol se formó hace unos **4,600 millones de años** a partir de una nube de gas y polvo.
        #- 🔭 Se encuentra **en la mitad de su vida** como estrella de tipo G (amarilla).
        #- ☄️ Formó el Sistema Solar a su alrededor con planetas, asteroides y cometas.
        #- 🕳️ En unos **5,000 millones de años**, se convertirá en una **gigante roja**, y después en una **enana blanca**.

        #📍 Actualmente, se encuentra en una etapa llamada **secuencia principal**: produce energía estable por fusión.

        #""")

        st.markdown(""" ## 🧬 Estructura del Sol
        """)

        
        # Mostrar imagen ilustrativa
        imagen = Image.open("im_04.png")
        st.image(imagen, caption="Capas del Sol", use_container_width=True)

        
        st.markdown("""

        El Sol está dividido en **capas**, desde el centro hacia afuera:

        ### 1. **Núcleo**
        - Temperatura: **~15 millones °C**
        - Lugar donde ocurre la **fusión nuclear**

        ### 2. **Zona radiativa**
        - La energía se transmite lentamente mediante radiación.
        - La luz puede tardar **cientos de miles de años** en salir de aquí.

        ### 3. **Zona convectiva**
        - Movimiento de gases calientes que ascienden y fríos que descienden.

        ### 4. **Fotosfera**
        - **“Superficie” visible del Sol**
        - Temperatura: ~5,500 °C
        - Aquí se observan las **manchas solares**.

        ### 5. **Cromosfera**
        - Capa rojiza, visible durante los eclipses solares.
        - Sede de explosiones como las **protuberancias solares**.

        ### 6. **Corona**    
        - Atmósfera externa del Sol, muy tenue y caliente (más de 1 millón °C).
        - Se ve como un halo blanco durante los eclipses.

        """)

        
#        st.markdown("""
#        ---

#        ## 🌍 Importancia del Sol para la Tierra

#        - Proporciona luz y calor esenciales para los ecosistemas.
#        - Influye en el **clima**, los **ciclos biológicos** y la **agricultura**.
#        - Su campo magnético protege a la Tierra del **viento solar**.
#        - Las variaciones en su actividad pueden afectar satélites y telecomunicaciones.

 #       """)

        st.title("🌑 ¿Qué son las manchas solares?")

        st.markdown("""
        Las **manchas solares** son zonas más frías y oscuras que aparecen sobre la **fotosfera** del Sol.  
        Aunque parecen negras, tienen temperaturas cercanas a los **3,500 °C**, en contraste con los **5,500 °C** del resto del disco solar.

        Estas regiones son temporales y están asociadas con una intensa actividad magnética del Sol.

        ---
        """)

        # Imagen estática con etiquetas
        st.markdown("### 🧬 Estructura de una mancha solar")
        st.markdown("""
        - **Umbra**: núcleo central, más oscuro y frío.  
        - **Penumbra**: anillo exterior, con textura filamentosa.  
        - Observa cómo ambas zonas están rodeadas por la **fotosfera**, donde también pueden verse los granos solares.
        """)

        imagen = Image.open("im_05.png")
        st.image(imagen, caption="Zonas en una mancha solar", use_container_width=True)

        # Explicación física
        st.markdown("""
        ---

        ### 🔍 ¿Por qué se forman?

        Las manchas solares se deben a **campos magnéticos intensos** que bloquean el flujo de energía térmica desde el interior del Sol.  
        Esto provoca que ciertas zonas se enfríen y oscurezcan respecto al entorno.

        ---

        ### 🔧 Evolución de una mancha

        A lo largo del tiempo, una mancha puede **fragmentarse**, **dispersarse** y **desaparecer**.  
        Este proceso depende del comportamiento del campo magnético.

        """)

        st.image("im_06.gif", caption="Fragmentación y erosión de una mancha solar")

        # Movimiento aparente desde la Tierra
        st.markdown("""
        ---

        ### 🌍 Movimiento aparente desde la Tierra

        Debido a la rotación de la Tierra, las manchas solares parecen desplazarse de **este a oeste** en la bóveda celeste, aunque en realidad están en la superficie solar.

        """)
        st.image("im_07.gif", caption="Movimiento aparente de las manchas solares causado por la rotación terrestre")

        # Movimiento real del Sol
        st.markdown("""
        ---

        ### ☀️ Movimiento real en el Sol

        La **rotación del Sol** (que es diferencial) hace que las manchas también se desplacen sobre su superficie.  
        Este movimiento es más rápido en el ecuador que en los polos.

        """)
        st.image("im_08.gif", caption="Movimiento real de las manchas solares sobre la superficie del Sol")

        # Ciclo solar
        st.markdown("""
        ---

        ### 🔄 Ciclo de las manchas solares

        Las manchas siguen un ciclo regular de aproximadamente **11 años**, en el que su número y posición cambian progresivamente.  
        Inicialmente surgen cerca de los polos solares y, con el tiempo, migran hacia el ecuador.

        """)
        st.image("im_09.gif", caption="Migración de las manchas solares durante el ciclo solar de 11 años")


        

        st.markdown("""
        ---

        ### 🌍 ¿Por qué son importantes?

        - Indican niveles de **actividad solar**
        - Se relacionan con **tormentas solares** que pueden afectar la Tierra
        - Aumentan durante el **máximo solar**, dentro de un ciclo de 11 años

        """)


        st.markdown("""
        ---

        ### 💡 ¿Sabías que...?

        - Galileo Galilei fue de los primeros en observarlas con telescopio.
        - Algunas manchas solares son **más grandes que la Tierra**.
        - Se clasifican y se cuentan con el **número de Wolf**.

        ---
        """)


        st.markdown("---")
        st.success("¡Ahora ya sabes más sobre nuestra estrella más cercana! Puedes continuar con el análisis de imágenes del Sol para ver sus manchas solares.")

        

        import streamlit as st
        from PIL import Image

        st.title("🧠 Detección de bordes: ¿Cómo encontramos las manchas solares?")

        st.markdown("""
        La **detección de bordes** es una técnica esencial del procesamiento de imágenes.  
        Nos permite encontrar los **límites de objetos** dentro de una imagen, como el borde del Sol y las manchas solares.

        ---

        ### 🧭 ¿Qué es un borde?

        Un **borde** es una zona donde hay un cambio abrupto de color o intensidad de luz.  
        El ojo humano lo reconoce como "límite" entre objetos, y los algoritmos también pueden hacerlo.

        En imágenes del Sol:
        - Los **bordes externos** permiten identificar el disco solar.
        - Las **manchas oscuras** internas también tienen bordes que permiten delimitar su forma y tamaño.

        ---

        ### 🎨 Ilustración del proceso

        A continuación puedes ver un resumen visual del proceso paso a paso:
        """)

        # Cargar imagen ilustrativa desde archivo local
        #imagen_ilustrativa = Image.open("/mnt/data/A_screenshot_of_an_educational_interface_in_Spanis.png")
        #st.image(imagen_ilustrativa, caption="Resumen visual del proceso de detección de bordes", use_column_width=True)

        st.markdown("""
        ---

        ### 🔍 Etapas del proceso

        1. **Imagen original**: la foto del Sol en color.
        2. **Escala de grises**: convertimos a blanco y negro para trabajar con intensidad.
        3. **Umbralización (binarización)**: dividimos la imagen en zonas claras (fondo) y oscuras (manchas).
        4. **Detección de bordes**: el algoritmo marca los límites de las regiones oscuras.

        ---
        """)
        
        st.image("im_12.gif", caption="proceso de detección de manchas solares mediante bordes")

        st.markdown(
        """
        ✅ ¡Ya tienes la base para entender cómo detectamos las manchas solares!  
        En la siguiente sección podrás aplicar este proceso a tu propia imagen y ajustar los parámetros manualmente.
        """)

    
    
    
    if page == "Visualizador de Imagen del Sol":
        import streamlit as st
        import cv2
        import numpy as np
        from PIL import Image
        import math
        import pandas as pd
        import streamlit.components.v1 as components
        import base64
        from io import BytesIO

 #       def show_image_with_zoom(image_np, caption="Imagen"):
 #           # Convertir imagen OpenCV a base64 para HTML
 #           image_pil = Image.fromarray(cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB))
 #           buffered = BytesIO()
 #           image_pil.save(buffered, format="PNG")
 #           img_str = base64.b64encode(buffered.getvalue()).decode()

 #           html_code = f"""
 #           <div style="overflow: auto; border: 1px solid #ccc; padding: 10px;">
 #               <p><strong>{caption}</strong></p>
 #               <img src="data:image/png;base64,{img_str}" style="width:100%; max-width:800px; transition: transform 0.2s;" 
 #                    onwheel="this.style.transform = `scale(${Math.max(1, parseFloat(this.style.transform.replace('scale(', '').replace(')', '')) + (event.deltaY < 0 ? 0.1 : -0.1))})`"
 #                    />
 #           </div>
 #           """
 #           components.html(html_code, height=600)

        def show_image_with_zoom(image_np, caption="Imagen"):
            # Convertir imagen OpenCV a base64 para HTML
            image_pil = Image.fromarray(cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB))
            buffered = BytesIO()
            image_pil.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()

            html_code = f"""
            <div style="overflow: auto; border: 1px solid #ccc; padding: 10px;">
                <p><strong>{caption}</strong></p>
                <img id="zoomable" src="data:image/png;base64,{img_str}" 
                     style="width:100%; max-width:800px; transition: transform 0.2s; transform: scale(1);" />
                <script>
                const img = window.parent.document.getElementById("zoomable");
                img.addEventListener("wheel", function(event) {{
                    event.preventDefault();
                    let scale = parseFloat(img.style.transform.replace('scale(', '').replace(')', '')) || 1;
                    scale += (event.deltaY < 0 ? 0.1 : -0.1);
                    scale = Math.max(1, Math.min(5, scale));
                    img.style.transform = `scale(${{scale}})`;
                }});
                </script>
            </div>
            """
            components.html(html_code, height=650)

        import plotly.graph_objects as go

        def mostrar_imagen_plotly(imagen_np, titulo="Imagen"):
            # Convertir de BGR a RGB
            imagen_rgb = cv2.cvtColor(imagen_np, cv2.COLOR_BGR2RGB)

            fig = go.Figure()

            fig.add_trace(go.Image(z=imagen_rgb))

            fig.update_layout(
                title=titulo,
                dragmode="pan",
                margin=dict(l=0, r=0, t=30, b=0),
                xaxis=dict(showgrid=False, zeroline=False),
                yaxis=dict(showgrid=False, zeroline=False, scaleanchor="x", scaleratio=1),
            )

            fig.update_xaxes(showticklabels=False)
            fig.update_yaxes(showticklabels=False)

            st.plotly_chart(fig, use_container_width=True)

        


#        st.title("Visualizador de Imagen del Sol")
#        st.write("Carga una imagen del sol y mírala aquí! (formatos posibles: .jpg, jpeg., .png)")

#        uploaded_file = st.file_uploader("Cargar imagen", type=["jpg", "jpeg", "png"])
#        st.write("Escribe tus datos sobre la imagen (evita el uso de acento)")
#        ksize = st.sidebar.slider("Tamaño del bloque (impares)", 3, 71, 11, step=2)
#        c = st.sidebar.slider("C", -10, 71, 2)


        st.title("Visualizador de Imagen del Sol")
        st.write("Carga una imagen del sol y mírala aquí! (formatos posibles: .jpg, .jpeg, .png)")

        uploaded_file = st.file_uploader("Cargar imagen", type=["jpg", "jpeg", "png"])

        # Mostrar opción de imagen de ejemplo solo si no se ha subido una
        use_example = False
        if uploaded_file is None:
            use_example = st.checkbox("Usar imagen de ejemplo", value=True)

        # Parámetros para el procesamiento (ya sea con imagen cargada o de ejemplo)
        ksize = st.sidebar.slider("Tamaño del bloque (impares)", 3, 71, 11, step=2)
        c = st.sidebar.slider("C", -10, 71, 2)


        
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Imagen cargada", use_container_width=True)
        else:
            image = Image.open("ejemplo240324.jpg")  # Imagen de ejemplo actual
            st.image(image, caption="Imagen de ejemplo", use_container_width=True)
            st.info("Se está utilizando una imagen de ejemplo.")
        
        #if uploaded_file is not None:
            # Mostrar la imagen cargada
        #    image = Image.open(uploaded_file)

            # Cajas de entrada para el autor, lugar y hora
            autor = st.text_input("Autor", "")
            lugar = st.text_input("Lugar", "")
            hora = st.text_input("Hora", "")
            fecha = st.text_input("Fecha", "")

            
            if st.button("Mostrar datos en imagen"):
                # Convertir la imagen cargada a una matriz numpy
                image_np = np.array(image.copy())

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
                # Encontrar el punto en el borde derecho del contorno del sol

                # Encontrar el punto en el borde derecho del contorno del sol
                rightmost_point = tuple(contorno_sol[contorno_sol[:, :, 0].argmax()][0])

                # Calcular el punto en la línea horizontal
                horizontal_point = (rightmost_point[0], centro_sol[1])

                # Aplicar umbralización adaptativa para detectar las manchas solares dentro del disco solar
                binary_manchas_solares = cv2.adaptiveThreshold(imagen_gris, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, ksize, c)

                # Encontrar contornos en la imagen binaria de las manchas solares
                contornos_manchas_solares, _ = cv2.findContours(binary_manchas_solares, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                # Crear una nueva imagen en blanco del mismo tamaño que la original
                #imagen_con_circulo = image_np.copy()

                # Dibujar el círculo que contiene el contorno del sol en la nueva imagen
                #cv2.circle(imagen_con_circulo, centro_sol, radio_sol, (0, 0, 255), 2)

                # Crear una nueva imagen en blanco del mismo tamaño que la original
                imagen_con_circulo = np.zeros_like(image_np)

                # Dibujar el círculo que contiene el contorno del sol en la nueva imagen
                cv2.circle(imagen_con_circulo, centro_sol, radio_sol, (0, 0, 255), 2)

                # Dibujar los contornos en la imagen en blanco
                cv2.drawContours(imagen_con_circulo, contornos_manchas_solares, -1, (0, 0, 255), 2)
                
                # Crear una imagen en blanco del mismo tamaño que la original
                imagen_contornos = np.zeros_like(image_np)

                # Dibujar el círculo que contiene el contorno del sol en la nueva imagen
                cv2.circle(imagen_contornos, centro_sol, radio_sol, (0, 0, 255), 2)
                # Dibujar los contornos en la imagen en blanco
                cv2.drawContours(imagen_contornos, contornos_manchas_solares, -1, (0, 0, 255), 2)
                


                import math

                # Definir el espacio entre los círculos concéntricos y las líneas radiales
                espacio = 0.2

                # Dibujar círculos concéntricos blancos
                for i in range(1, int(radio_sol), int(espacio * radio_sol)):
                    cv2.circle(imagen_contornos, centro_sol, i, (255, 255, 255), 1, cv2.LINE_AA)

                # Dibujar líneas radiales
                for angulo in range(0, 360, 15):
                    x = int(centro_sol[0] + radio_sol * math.cos(math.radians(angulo)))
                    y = int(centro_sol[1] + radio_sol * math.sin(math.radians(angulo)))
                    cv2.line(imagen_contornos, centro_sol, (x, y), (255, 255, 255), 1, cv2.LINE_AA)



                
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

                # Dibujar los contornos de las manchas solares dentro del disco solar en la nueva imagen
                for contorno in contornos_manchas_solares:
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

                        # Dibujar el contorno etiquetado
                        cv2.putText(imagen_contornos, str(nueva_etiqueta), (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

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

                # Dibujar texto en la imagen
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottom_left_corner = (10, image_np.shape[0] - 10)
                font_scale = 0.8
                font_color = (255, 255, 255)
                line_type = 1
    
                cv2.putText(imagen_con_circulo, f"Autor: {autor}", bottom_left_corner, font, font_scale, font_color, line_type, cv2.LINE_AA)
                cv2.putText(imagen_con_circulo, f"Lugar: {lugar}", (bottom_left_corner[0], bottom_left_corner[1] - 30), font, font_scale, font_color, line_type, cv2.LINE_AA)
                cv2.putText(imagen_con_circulo, f"Hora: {hora}", (bottom_left_corner[0], bottom_left_corner[1] - 60), font, font_scale, font_color, line_type, cv2.LINE_AA)
                cv2.putText(imagen_con_circulo, f"Fecha: {fecha}", (bottom_left_corner[0], bottom_left_corner[1] - 90), font, font_scale, font_color, line_type, cv2.LINE_AA)
                cv2.line(imagen_con_circulo, centro_sol, horizontal_point, (255, 255, 255), 1)
                radio_text = f"Radio del Sol: {radio_sol} pixeles"
                cv2.putText(imagen_con_circulo, radio_text, (horizontal_point[0], horizontal_point[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

                
                # Dibujar texto en la imagen con contornos etiquetados
                

                cv2.putText(imagen_contornos, f"Autor: {autor}", bottom_left_corner, font, font_scale, font_color, line_type, cv2.LINE_AA)
                cv2.putText(imagen_contornos, f"Lugar: {lugar}", (bottom_left_corner[0], bottom_left_corner[1] - 30), font, font_scale, font_color, line_type, cv2.LINE_AA)
                cv2.putText(imagen_contornos, f"Hora: {hora}", (bottom_left_corner[0], bottom_left_corner[1] - 60), font, font_scale, font_color, line_type, cv2.LINE_AA)
                cv2.putText(imagen_contornos, f"Fecha: {fecha}", (bottom_left_corner[0], bottom_left_corner[1] - 90), font, font_scale, font_color, line_type, cv2.LINE_AA)
                cv2.line(imagen_contornos, centro_sol, horizontal_point, (255, 255, 255), 2)
                # Dibujar el texto del radio del sol sobre la línea horizontal
                radio_text = f"Radio del Sol: {radio_sol} pixeles"
                cv2.putText(imagen_contornos, radio_text, (horizontal_point[0], horizontal_point[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

                
                # Dibujar texto en la imagen original
                cv2.putText(image_np, f"Autor: {autor}", bottom_left_corner, font, font_scale, font_color, line_type, cv2.LINE_AA)
                cv2.putText(image_np, f"Lugar: {lugar}", (bottom_left_corner[0], bottom_left_corner[1] - 30), font, font_scale, font_color, line_type, cv2.LINE_AA)
                cv2.putText(image_np, f"Hora: {hora}", (bottom_left_corner[0], bottom_left_corner[1] - 60), font, font_scale, font_color, line_type, cv2.LINE_AA)
                cv2.putText(image_np, f"Fecha: {fecha}", (bottom_left_corner[0], bottom_left_corner[1] - 90), font, font_scale, font_color, line_type, cv2.LINE_AA)


                # Mostrar las tres imágenes
                st.image(image_np, caption="Imagen subida", use_container_width=True)
                with st.expander("Guía para ajustar los contornos del Sol y las manchas solares"):
                    st.markdown("""
                
                    Al cargar una imagen, es posible que los **contornos no se vean correctamente al principio**. Esto es normal y puede corregirse usando los deslizadores en la barra lateral.

                    ---

                    #### 🎚️ Tamaño del bloque (`ksize`)
                    - Define el tamaño del área local analizada para detectar sombras.
                    - Debe ser un **número impar** (ej. 11, 15, 21).
                    - **Pequeños valores** detectan detalles finos pero pueden generar ruido.
                    - **Valores grandes** suavizan el resultado, útil si hay muchas sombras o reflejos.

                    #### 🎚️ Constante `C`
                    - Se **resta del brillo promedio local**.
                    - **Mayor C** reduce ruido excesivo.
                    - **Menor C** ayuda a detectar manchas más débiles.
                    ---

                    #### ✅ Recomendación inicial:
                    - Comienza con:
                    - `ksize = 11`
                    - `C = 2`
                    - Si no ves bordes definidos:
                      - Prueba con `ksize = 15`, `C = 5`
                      - O `ksize = 21`, `C = 10`
                    ---
                """)


                
                st.image(imagen_con_circulo, caption="Imagen con contornos", use_container_width=True)
                #show_image_with_zoom(imagen_con_circulo, caption="Imagen con contornos")
                #mostrar_imagen_plotly(imagen_contornos, "Imagen con contornos etiquetados")

                st.image(imagen_contornos, caption="Imagen con contornos etiquetados", use_container_width=True)

                # Mostrar el radio del Sol en kilómetros
                radio_sol_km = round(radio_sol * (696340 / radio_sol), 2)  # Equivale directamente a 696340 km
                radio_sol_km = 696340  # siempre es el real
                km_por_pixel = radio_sol_km / radio_sol
                st.markdown(f"🌞 **Radio solar estimado en la imagen:** {radio_sol_km:,} km")
                st.markdown(f"🌞 **Radio solar real:** {radio_sol_km:,} km")
                st.markdown(f"📏 **Escala de la imagen:** 1 pixel ≈ {km_por_pixel:.2f} km")

                
                # Mostrar el DataFrame
                st.write("Información de los contornos:")
                #st.write(df)

                # Constante del radio del Sol en kilómetros
                RADIO_SOL_KM = 696340  # km

                def convertir_pixeles_a_km2(df, radio_sol_pixeles):
                    df_km = df.copy()
                    factor_escala = (RADIO_SOL_KM / radio_sol_pixeles) ** 2  # (km/pix)^2

                    df_km["Tamaño (km²)"] = df_km["Tamaño (pix^2)"] * factor_escala
                    df_km["Distancia Radial (km)"] = df_km["Distancia Radial (pix)"] * (RADIO_SOL_KM / radio_sol_pixeles)

                    return df_km[[
                        "Contorno", "Centro_X (pixeles)", "Centro_Y (pixeles)",
                        "Tamaño (km²)", "Distancia Radial (km)", "Ángulo (grados)"
                    ]]

                # Aplicar conversión si existe DataFrame y radio del Sol en píxeles
                df_km = convertir_pixeles_a_km2(df, radio_sol_pixeles=radio_sol)

                st.write("🧭 Información de contornos solares en unidades reales:")
                st.write(df_km)



    #########

    elif page == "Visualizador de Eclipse":
        import cv2
        import numpy as np
        #import numpy as np
        import matplotlib.pyplot as plt
        from matplotlib.patches import Circle
        from PIL import Image
        import shapely.geometry as sg
        #import streamlit as st



        import streamlit as st
        from PIL import Image
        import cv2
        import numpy as np

        st.title("Visualizador de Eclipse")
        st.write("Esta es la página del visualizador de eclipse. Aquí puedes cargar o seleccionar una imagen del eclipse solar.")

        # Cargar imagen del usuario
        st.write("📷 **Carga una imagen del eclipse** (formatos permitidos: .jpg, .jpeg, .png):")
        uploaded_file = st.file_uploader("Cargar imagen", type=["jpg", "jpeg", "png"])

        # Si no se carga imagen, mostrar selector de ejemplo
        example_image = None
        fase_eclipse = ""
        if uploaded_file is None:
            opcion = st.selectbox("O selecciona una imagen de ejemplo:", (
                "Ninguna",
                "Inicio del eclipse (eclipse080424i)",
                "Durante el eclipse (eclipse080424m)",
                "Final del eclipse (eclipse080424f)"
            ))

            if opcion == "Inicio del eclipse (eclipse080424i)":
                example_image = "eclipse080424i.jpg"
                fase_eclipse = (
                    "🌒 **Inicio del eclipse:** Aquí comienza la ocultación del Sol por la Luna. "
                    "Es posible ver cómo el disco lunar empieza a 'morder' al Sol desde un borde."
                )
            elif opcion == "Durante el eclipse (eclipse080424m)":
                example_image = "eclipse080424m.jpg"
                fase_eclipse = (
                    "🌕 **Máximo del eclipse:** La Luna cubre la mayor parte del Sol observable desde el punto de captura. "
                    "Es el momento más impresionante visualmente."
                )
            elif opcion == "Final del eclipse (eclipse080424f)":
                example_image = "eclipse080424f.jpg"
                fase_eclipse = (
                    "🌘 **Final del eclipse:** El disco lunar se aleja lentamente del Sol. "
                    "La silueta solar vuelve a verse completa poco a poco."
                )

        # Determinar la fuente final de imagen    
        image_file = uploaded_file if uploaded_file else example_image
        caption_text = "Imagen cargada" if uploaded_file else f"Ejemplo: {example_image}" if example_image else ""

        # Si hay imagen válida, procesar
        if image_file:
            image = Image.open(image_file)
            st.image(image, caption=caption_text, use_container_width=True)

            if example_image:
                st.info(f"Se está utilizando la imagen de ejemplo: {example_image}")
                st.markdown(fase_eclipse)

            # Ahora puedes convertirla a formato OpenCV sin error
            image_bgr = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        


        #import streamlit as st
        #from PIL import Image
        #import cv2
        #import numpy as np

        #st.title("Visualizador de Eclipse")
        #st.write("Esta es la página del visualizador de eclipse. Aquí puedes cargar o seleccionar una imagen del eclipse solar.")

        # Cargar imagen del usuario
        #st.write("📷 **Carga una imagen del eclipse** (formatos permitidos: .jpg, .jpeg, .png):")
        #uploaded_file = st.file_uploader("Cargar imagen", type=["jpg", "jpeg", "png"])

        ## Si no se carga imagen, mostrar selector de ejemplo
        #example_image = None
        #fase_eclipse = ""
        #if uploaded_file is None:
        #    opcion = st.selectbox("O selecciona una imagen de ejemplo:", (
        #        "Ninguna",
        #        "Inicio del eclipse (eclipse080424i)",
        #        "Durante el eclipse (eclipse080424m)",
        #        "Final del eclipse (eclipse080424f)"
        #    ))

       #     if opcion == "Inicio del eclipse (eclipse080424i)":
       #         example_image = "eclipse080424i.jpg"
       #         fase_eclipse = (
       #             "🌒 **Inicio del eclipse:** Aquí comienza la ocultación del Sol por la Luna. "
       #             "Es posible ver cómo el disco lunar empieza a 'morder' al Sol desde un borde."
       #         )
       #     elif opcion == "Durante el eclipse (eclipse080424m)":
       #         example_image = "eclipse080424m.jpg"
       #         fase_eclipse = (
       #             "🌕 **Máximo del eclipse:** La Luna cubre la mayor parte del Sol observable desde el punto de captura. "
       #             "Es el momento más impresionante visualmente."
       #         )
       #     elif opcion == "Final del eclipse (eclipse080424f)":
       #         example_image = "eclipse080424f.jpg"
       #         fase_eclipse = (
       #             "🌘 **Final del eclipse:** El disco lunar se aleja lentamente del Sol. "
       #             "La silueta solar vuelve a verse completa poco a poco."
       #         )
       # # Determinar la fuente final de imagen
       # if uploaded_file is not None:
       #     image_file = uploaded_file
       #     caption_text = "Imagen cargada"
       # elif example_image is not None:
       #     image_file = example_image
       #     caption_text = f"Ejemplo: {example_image}"
       # else:
       #     image_file = None
       #     st.warning("Por favor, carga una imagen o selecciona una de ejemplo.")

        
        # Mostrar imagen cargada o ejemplo
        #if uploaded_file is not None:
        #    image = Image.open(uploaded_file)
        #    st.image(image, caption="Imagen cargada", use_column_width=True)
        #elif example_image is not None:
        #    image = Image.open(example_image)
        #    st.image(image, caption=f"Ejemplo: {example_image}", use_column_width=True)
        #    st.info(f"Se está utilizando la imagen de ejemplo: {example_image}")
        #    st.markdown(fase_eclipse)
        #else:
        #    st.warning("Por favor, carga una imagen o selecciona una de ejemplo.")

        # Si hay imagen válida, continuar con la app
        #if uploaded_file is not None or example_image is not None:
        #if image_file is not None or example_image is not None:
          
        #    image_bgr = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

            # Entradas para metadatos
            #st.text_input("Autor", key="autor")
            #st.text_input("Lugar", key="lugar")
            #st.text_input("Hora", key="hora")
            #st.text_input("Fecha", key="fecha")







        
        #st.title("Visualizador de Eclipse")
        #st.write("Esta es la página del visualizador de eclipse. Aquí puedes agregar el código para visualizar eclipses.")

        #st.write("Carga una imagen del sol y mírala aquí! (formatos posibles: .jpg, jpeg., .png)")

        #uploaded_file = st.file_uploader("Cargar imagen", type=["jpg", "jpeg", "png"])
        #st.write("Escribe tus datos sobre la imagen (evita el uso de acento)")

        #if uploaded_file is not None:
        #    # Mostrar la imagen cargada
        #    image = Image.open(uploaded_file)
        
        #    # Convertir la imagen RGB a formato BGR
        #    image_bgr = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

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
                st.image(imagen_with_text, caption="Fotografía del Sol durante el eclipse", use_container_width=True)
                
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
#            img = Image.open(uploaded_file)
            img = Image.open(image_file)

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

        with st.sidebar:
            pos_x1 = st.slider('PosX1', -30.0, 30.0, 0.0, 0.1)
            pos_y1 = st.slider('PosY1', -30.0, 30.0, 0.0, 0.1)
            radio1 = st.slider('Radio1', 0.0, 20.0, 10.0, 0.1)
            pos_x2 = st.slider('PosX2', -30.0, 30.0, 5.0, 0.1)
            pos_y2 = st.slider('PosY2', -30.0, 30.0, 5.0, 0.1)
            radio2 = st.slider('Radio2', 0.0, 20.0, 7.0, 0.1)
            x_limit = st.slider('Límite X', 1.0, 50.0, 30.0, 1.0)
            y_limit = st.slider('Límite Y', 1.0, 50.0, 30.0, 1.0)

        
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
            st.image(imagen_with_text, caption="Fotografía del Sol durante el eclipse", use_container_width=True)


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

        def simulate_eclipse_lighting(image, eclipse_strength):
            """
            Ajusta la imagen simulando la iluminación durante un eclipse.
            :param image: imagen RGB (uint8)
            :param eclipse_strength: 0.0 (sin eclipse) a 1.0 (totalmente oscuro)
            :return: imagen ajustada
            """
            # Convertir a float para operaciones suaves
            img_float = image.astype(np.float32) / 255.0

            # Oscurecer suavemente
            darkened = img_float * (1.0 - 0.5 * eclipse_strength)  # solo hasta 50% menos brillo

            # Aplicar tono azul-gris (sombra fría)
            cool_filter = np.array([0.9, 0.95, 1.0])  # ligeramente azulada
            tinted = darkened * (1 - 0.3 * eclipse_strength + 0.3 * eclipse_strength * cool_filter)

            # Asegurar límites y convertir de nuevo
            tinted = np.clip(tinted * 255, 0, 255).astype(np.uint8)
            return tinted


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
                #brightened_image = decrease_brightness(image_rgb, brightness_adjustment)
                # Calcular fuerza del eclipse como fracción (1.0 = eclipse total, 0.0 = sin eclipse)
                #eclipse_strength = 1.0 - (percentage_area_not_in_intersection / 100.0)
                eclipse_strength = 1.0 - (percentage_area_not_in_intersection / 100.0)
                brightened_image = simulate_eclipse_lighting(image_rgb, eclipse_strength)

                # Simular iluminación
                #brightened_image = simulate_eclipse_lighting(image_rgb, eclipse_strength)

                #brightened_image = simulate_eclipse_lighting(image_rgb, brightness_adjustment)
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
        import base64


        import streamlit as st
        import base64



        import os
        import base64
        import streamlit as st

        gif_path = "eclipse_coloreado_natural.gif"

        if os.path.exists(gif_path):
            with open(gif_path, "rb") as f:
                gif_bytes = f.read()
                encoded = base64.b64encode(gif_bytes).decode("utf-8")

            st.markdown(
                f"""
                <figure style="text-align: center;">
                    <img src="data:image/gif;base64,{encoded}" width="600">
                    <figcaption style="font-size: 0.9em; color: gray; margin-top: 5px;">
                        Secuencia fotográfica tomada durante el eclipse del 08 de abril de 2024 (desde Colima, México) 
                    </figcaption>
                </figure>
                """,
                unsafe_allow_html=True
            )
        else:
            st.error("❌ No se encontró el archivo GIF.")

        
  
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


## Crear un mapa centrado en Estados Unidos
#usa_map = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

        # Coordenadas proporcionadas
        coordinates_norte = [
            (6 + (11.7 / 60), -(146 + (38.0 / 60))), (5 + (8.4 / 60), -(143 + (0.6 / 60))),
            (4 + (12.3 / 60), -(140 + (15.6 / 60))), (3 + (20.2 / 60), -(137 + (59.5 / 60))),
            (2 + (30.8 / 60), -(136 + (2.5 / 60))), (1 + (43.4 / 60), -(134 + (19.0 / 60))),
            (0 + (57.6 / 60), -(132 + (45.9 / 60))), (0 + (13.0 / 60), -(131 + (21.1 / 60))),
            (0 + (30.6 / 60), -(130 + (3.0 / 60))), (1 + (13.2 / 60), -(128 + (50.5 / 60))),
            (1 + (55.1 / 60), -(127 + (42.8 / 60))), (2 + (36.4 / 60), -(126 + (39.1 / 60))),
            (3 + (17.0 / 60), -(125 + (39.0 / 60))), (3 + (57.2 / 60), -(124 + (42.0 / 60))),
            (4 + (36.8 / 60), -(123 + (47.8 / 60))), (5 + (16.0 / 60), -(122 + (56.0 / 60))),
            (5 + (54.8 / 60), -(122 + (6.4 / 60))), (6 + (33.3 / 60), -(121 + (18.7 / 60))),
            (7 + (11.4 / 60), -(120 + (32.8 / 60))), (7 + (49.2 / 60), -(119 + (48.5 / 60))),
            (8 + (26.8 / 60), -(119 + (5.7 / 60))), (9 + (4.0 / 60), -(118 + (24.2 / 60))),
            (9 + (41.1 / 60), -(117 + (43.8 / 60))), (10 + (17.9 / 60), -(117 + (4.6 / 60))),
            (10 + (54.4 / 60), -(116 + (26.3 / 60))), (11 + (30.8 / 60), -(115 + (49.0 / 60))),
            (12 + (7.0 / 60), -(115 + (12.4 / 60))), (12 + (43.0 / 60), -(114 + (36.6 / 60))),
            (13 + (18.9 / 60), -(114 + (1.4 / 60))), (13 + (54.6 / 60), -(113 + (26.8 / 60))),
            (14 + (30.1 / 60), -(112 + (52.8 / 60))), (15 + (5.5 / 60), -(112 + (19.2 / 60))),
            (15 + (40.8 / 60), -(111 + (46.0 / 60))), (16 + (15.9 / 60), -(111 + (13.3 / 60))),
            (16 + (51.0 / 60), -(110 + (40.8 / 60))), (17 + (25.9 / 60), -(110 + (8.6 / 60))),
            (18 + (0.7 / 60), -(109 + (36.6 / 60))), (18 + (35.4 / 60), -(109 + (4.8 / 60))),
            (19 + (10.1 / 60), -(108 + (33.1 / 60))), (19 + (44.6 / 60), -(108 + (1.5 / 60))),
            (20 + (19.1 / 60), -(107 + (29.9 / 60))), (20 + (53.5 / 60), -(106 + (58.4 / 60))),
            (21 + (27.8 / 60), -(106 + (26.8 / 60))), (22 + (2.0 / 60), -(105 + (55.1 / 60))),
            (22 + (36.2 / 60), -(105 + (23.3 / 60))), (23 + (10.3 / 60), -(104 + (51.4 / 60))),
            (23 + (44.4 / 60), -(104 + (19.2 / 60))), (24 + (18.4 / 60), -(103 + (46.8 / 60))),
            (24 + (52.3 / 60), -(103 + (14.2 / 60))), (25 + (26.3 / 60), -(102 + (41.2 / 60))),
            (26 + (0.1 / 60), -(102 + (7.8 / 60))), (26 + (33.9 / 60), -(101 + (34.0 / 60))),
            (27 + (7.7 / 60), -(100 + (59.8 / 60))), (27 + (41.4 / 60), -(100 + (25.1 / 60))),
            (28 + (15.1 / 60), -(99 + (49.8 / 60))), (28 + (48.8 / 60), -(99 + (13.9 / 60))),
            (29 + (22.4 / 60), -(98 + (37.4 / 60))), (29 + (56.0 / 60), -(98 + (0.1 / 60))),
            (30 + (29.6 / 60), -(97 + (22.1 / 60))), (31 + (3.1 / 60), -(96 + (43.3 / 60))),
            (31 + (36.6 / 60), -(96 + (3.6 / 60))), (32 + (10.0 / 60), -(95 + (23.0 / 60))),
            (32 + (43.4 / 60), -(94 + (41.3 / 60))), (33 + (16.8 / 60), -(93 + (58.5 / 60))),
            (33 + (50.1 / 60), -(93 + (14.6 / 60))), (34 + (23.4 / 60), -(92 + (29.5 / 60))),
            (34 + (56.6 / 60), -(91 + (43.0 / 60))), (35 + (29.8 / 60), -(90 + (55.0 / 60))),
            (36 + (2.9 / 60), -(90 + (5.6 / 60))), (36 + (36.0 / 60), -(89 + (14.5 / 60))),
            (37 + (9.0 / 60), -(88 + (21.6 / 60))), (37 + (41.9 / 60), -(87 + (26.9 / 60))),
            (38 + (14.7 / 60), -(86 + (30.1 / 60))), (38 + (47.4 / 60), -(85 + (31.1 / 60))),
            (39 + (19.9 / 60), -(84 + (29.8 / 60))), (39 + (52.4 / 60), -(83 + (26.0 / 60))),
            (40 + (24.7 / 60), -(82 + (19.4 / 60))), (40 + (56.8 / 60), -(81 + (9.9 / 60))),
            (41 + (28.7 / 60), -(79 + (57.1 / 60))), (42 + (0.4 / 60), -(78 + (40.9 / 60))),
            (42 + (31.8 / 60), -(77 + (20.8 / 60))), (43 + (2.9 / 60), -(75 + (56.5 / 60))),
            (43 + (33.7 / 60), -(74 + (27.6 / 60))), (44 + (4.0 / 60), -(72 + (53.5 / 60))),
            (44 + (33.8 / 60), -(71 + (13.8 / 60))), (45 + (3.0 / 60), -(69 + (27.7 / 60))),
            (45 + (31.6 / 60), -(67 + (34.4 / 60))), (45 + (59.3 / 60), -(65 + (32.8 / 60))),
            (46 + (26.0 / 60), -(63 + (21.8 / 60))), (46 + (51.5 / 60), -(60 + (59.6 / 60))),
            (47 + (15.4 / 60), -(58 + (24.0 / 60))), (47 + (37.4 / 60), -(55 + (32.1 / 60))),
            (47 + (56.9 / 60), -(52 + (19.4 / 60))), (48 + (12.7 / 60), -(48 + (38.8 / 60))),
            (48 + (23.3 / 60), -(44 + (17.7 / 60))), (48 + (24.7 / 60), -(38 + (48.5 / 60)))
        ]


        # Coordenadas proporcionadas
        coordinates_sur = [
            (5 + (30.6 / 60), -(149 + (47.6 / 60))), (4 + (20.5 / 60), -(145 + (29.6 / 60))),
            (3 + (21.2 / 60), -(142 + (27.6 / 60))), (2 + (27.1 / 60), -(140 + (1.8 / 60))),
            (1 + (36.2 / 60), -(137 + (58.5 / 60))), (0 + (47.7 / 60), -(136 + (10.6 / 60))),
            (0 + (1.0 / 60), -(134 + (34.2 / 60))), (0 + (44.4 / 60), -(133 + (6.9 / 60))),
            (1 + (28.6 / 60), -(131 + (46.8 / 60))), (2 + (11.8 / 60), -(130 + (32.7 / 60))),
            (2 + (54.2 / 60), -(129 + (23.6 / 60))), (3 + (35.9 / 60), -(128 + (18.8 / 60))),
            (4 + (17.0 / 60), -(127 + (17.7 / 60))), (4 + (57.5 / 60), -(126 + (19.9 / 60))),
            (5 + (37.5 / 60), -(125 + (24.9 / 60))), (6 + (17.1 / 60), -(124 + (32.5 / 60))),
            (6 + (56.3 / 60), -(123 + (42.4 / 60))), (7 + (35.0 / 60), -(122 + (54.2 / 60))),
            (8 + (13.5 / 60), -(122 + (7.9 / 60))), (8 + (51.6 / 60), -(121 + (23.2 / 60))),
            (9 + (29.4 / 60), -(120 + (40.0 / 60))), (10 + (7.0 / 60), -(119 + (58.1 / 60))),
            (10 + (44.3 / 60), -(119 + (17.5 / 60))), (11 + (21.4 / 60), -(118 + (37.9 / 60))),
            (11 + (58.3 / 60), -(117 + (59.4 / 60))), (12 + (34.9 / 60), -(117 + (21.7 / 60))),
            (13 + (11.4 / 60), -(116 + (44.9 / 60))), (13 + (47.8 / 60), -(116 + (8.8 / 60))),
            (14 + (23.9 / 60), -(115 + (33.4 / 60))), (14 + (59.9 / 60), -(114 + (58.5 / 60))),
            (15 + (35.8 / 60), -(114 + (24.3 / 60))), (16 + (11.6 / 60), -(113 + (50.4 / 60))),
            (16 + (47.2 / 60), -(113 + (17.0 / 60))), (17 + (22.7 / 60), -(112 + (44.0 / 60))),
            (17 + (58.1 / 60), -(112 + (11.3 / 60))), (18 + (33.4 / 60), -(111 + (38.8 / 60))),
            (19 + (8.6 / 60), -(111 + (6.5 / 60))), (19 + (43.7 / 60), -(110 + (34.4 / 60))),
            (20 + (18.8 / 60), -(110 + (2.5 / 60))), (20 + (53.8 / 60), -(109 + (30.6 / 60))),
            (21 + (28.7 / 60), -(108 + (58.7 / 60))), (22 + (3.5 / 60), -(108 + (26.8 / 60))),
            (22 + (38.3 / 60), -(107 + (54.9 / 60))), (23 + (13.0 / 60), -(107 + (22.8 / 60))),
            (23 + (47.7 / 60), -(106 + (50.7 / 60))), (24 + (22.3 / 60), -(106 + (18.3 / 60))),
            (24 + (56.9 / 60), -(105 + (45.7 / 60))), (25 + (31.4 / 60), -(105 + (12.9 / 60))),
            (26 + (5.9 / 60), -(104 + (39.8 / 60))), (26 + (40.4 / 60), -(104 + (6.3 / 60))),
            (27 + (14.8 / 60), -(103 + (32.4 / 60))), (27 + (49.2 / 60), -(102 + (58.0 / 60))),
            (28 + (23.6 / 60), -(102 + (23.2 / 60))), (28 + (57.9 / 60), -(101 + (47.8 / 60))),
            (29 + (32.2 / 60), -(101 + (11.9 / 60))), (30 + (6.5 / 60), -(100 + (35.3 / 60))),
            (30 + (40.8 / 60), -(99 + (57.9 / 60))), (31 + (15.0 / 60), -(99 + (19.9 / 60))),
            (31 + (49.3 / 60), -(98 + (41.0 / 60))), (32 + (23.5 / 60), -(98 + (1.3 / 60))),
            (32 + (57.6 / 60), -(97 + (20.6 / 60))), (33 + (31.8 / 60), -(96 + (38.8 / 60))),
            (34 + (5.9 / 60), -(95 + (56.0 / 60))), (34 + (40.0 / 60), -(95 + (12.1 / 60))),
            (35 + (14.1 / 60), -(94 + (26.9 / 60))), (35 + (48.1 / 60), -(93 + (40.3 / 60))),
            (36 + (22.1 / 60), -(92 + (52.3 / 60))), (36 + (56.0 / 60), -(92 + (2.8 / 60))),
            (37 + (29.9 / 60), -(91 + (11.6 / 60))), (38 + (3.8 / 60), -(90 + (18.7 / 60))),
            (38 + (37.5 / 60), -(89 + (23.9 / 60))), (39 + (11.2 / 60), -(88 + (27.0 / 60))),
            (39 + (44.8 / 60), -(87 + (27.9 / 60))), (40 + (18.2 / 60), -(86 + (26.5 / 60))),
            (40 + (51.6 / 60), -(85 + (22.6 / 60))), (41 + (24.8 / 60), -(84 + (15.9 / 60))),
            (41 + (57.8 / 60), -(83 + (6.3 / 60))), (42 + (30.6 / 60), -(81 + (53.4 / 60))),
            (43 + (3.2 / 60), -(80 + (37.0 / 60))), (43 + (35.6 / 60), -(79 + (16.9 / 60))),
            (44 + (7.6 / 60), -(77 + (52.5 / 60))), (44 + (39.3 / 60), -(76 + (23.6 / 60))),
            (45 + (10.6 / 60), -(74 + (49.6 / 60))), (45 + (41.4 / 60), -(73 + (10.0 / 60))),
            (46 + (11.6 / 60), -(71 + (24.2 / 60))), (46 + (41.1 / 60), -(69 + (31.3 / 60))),
            (47 + (9.8 / 60), -(67 + (30.4 / 60))), (47 + (37.5 / 60), -(65 + (20.4 / 60))),
            (48 + (4.0 / 60), -(62 + (59.9 / 60))), (48 + (29.1 / 60), -(60 + (26.8 / 60))),
            (48 + (52.2 / 60), -(57 + (38.5 / 60))), (49 + (13.0 / 60), -(54 + (31.6 / 60))),
            (49 + (30.6 / 60), -(51 + (00.3 / 60))), (49 + (43.5 / 60), -(46 + (55.5 / 60))),
            (49 + (49.3 / 60), -(41 + (59.5 / 60))), (49 + (41.3 / 60), -(35 + (27.0 / 60)))
        ]

        # Coordenadas proporcionadas
        coordinates_centro = [
            (5 + (50.2 / 60), -(148 + (7.8 / 60))), (4 + (44.0 / 60), -(144 + (13.0 / 60))),
            (3 + (46.4 / 60), -(141 + (20.3 / 60))), (2 + (53.3 / 60), -(138 + (59.7 / 60))),
            (2 + (3.3 / 60), -(136 + (59.7 / 60))), (1 + (15.4 / 60), -(135 + (14.1 / 60))),
            (0 + (29.1 / 60), -(133 + (39.5 / 60))), (0 + (15.9 / 60), -(132 + (13.5 / 60))),
            (0 + (59.7 / 60), -(130 + (54.5 / 60))), (1 + (42.7 / 60), -(129 + (41.2 / 60))),
            (2 + (24.8 / 60), -(128 + (32.8 / 60))), (3 + (6.3 / 60), -(127 + (28.6 / 60))),
            (3 + (47.2 / 60), -(126 + (28.0 / 60))), (4 + (27.5 / 60), -(125 + (30.6 / 60))),
            (5 + (7.3 / 60), -(124 + (36.1 / 60))), (5 + (46.7 / 60), -(123 + (44.0 / 60))),
            (6 + (25.6 / 60), -(122 + (54.1 / 60))), (7 + (4.3 / 60), -(122 + (6.2 / 60))),
            (7 + (42.5 / 60), -(121 + (20.1 / 60))), (8 + (20.5 / 60), -(120 + (35.6 / 60))),
            (8 + (58.2 / 60), -(119 + (52.6 / 60))), (9 + (35.6 / 60), -(119 + (10.9 / 60))),
            (10 + (12.7 / 60), -(118 + (30.4 / 60))), (10 + (49.7 / 60), -(117 + (51.0 / 60))),
            (11 + (26.4 / 60), -(117 + (12.6 / 60))), (12 + (2.9 / 60), -(116 + (35.1 / 60))),
            (12 + (39.3 / 60), -(115 + (58.4 / 60))), (13 + (15.4 / 60), -(115 + (22.5 / 60))),
            (13 + (51.4 / 60), -(114 + (47.2 / 60))), (14 + (27.3 / 60), -(114 + (12.5 / 60))),
            (15 + (3.0 / 60), -(113 + (38.3 / 60))), (15 + (38.6 / 60), -(113 + (4.6 / 60))),
            (16 + (14.0 / 60), -(112 + (31.4 / 60))), (16 + (49.3 / 60), -(111 + (58.4 / 60))),
            (17 + (24.5 / 60), -(111 + (25.8 / 60))), (17 + (59.6 / 60), -(110 + (53.5 / 60))),
            (18 + (34.7 / 60), -(110 + (21.4 / 60))), (19 + (9.6 / 60), -(109 + (49.4 / 60))),
            (19 + (44.4 / 60), -(109 + (17.6 / 60))), (20 + (19.2 / 60), -(108 + (45.8 / 60))),
            (20 + (53.8 / 60), -(108 + (14.1 / 60))), (21 + (28.5 / 60), -(107 + (42.4 / 60))),
            (22 + (3.0 / 60), -(107 + (10.7 / 60))), (22 + (37.5 / 60), -(106 + (38.8 / 60))),
            (23 + (11.9 / 60), -(106 + (6.8 / 60))), (23 + (46.3 / 60), -(105 + (34.7 / 60))),
            (24 + (20.6 / 60), -(105 + (2.3 / 60))), (24 + (54.8 / 60), -(104 + (29.7 / 60))),
            (25 + (29.1 / 60), -(103 + (56.8 / 60))), (26 + (3.3 / 60), -(103 + (23.6 / 60))),
            (26 + (37.4 / 60), -(102 + (49.9 / 60))), (27 + (11.5 / 60), -(102 + (15.9 / 60))),
            (27 + (45.6 / 60), -(101 + (41.4 / 60))), (28 + (19.6 / 60), -(101 + (6.3 / 60))),
            (28 + (53.6 / 60), -(100 + (30.7 / 60))), (29 + (27.6 / 60), -(99 + (54.5 / 60))),
            (30 + (1.5 / 60), -(99 + (17.5 / 60))), (30 + (35.4 / 60), -(98 + (39.9 / 60))),
            (31 + (9.3 / 60), -(98 + (1.5 / 60))), (31 + (43.2 / 60), -(97 + (22.2 / 60))),
            (32 + (17.0 / 60), -(96 + (42.0 / 60))), (32 + (50.8 / 60), -(96 + (0.8 / 60))),
            (33 + (24.6 / 60), -(95 + (18.6 / 60))), (33 + (58.3 / 60), -(94 + (35.2 / 60))),
            (34 + (32.0 / 60), -(93 + (50.7 / 60))), (35 + (5.6 / 60), -(93 + (4.8 / 60))),
            (35 + (39.2 / 60), -(92 + (17.6 / 60))), (36 + (12.8 / 60), -(91 + (28.9 / 60))),
            (36 + (46.3 / 60), -(90 + (38.6 / 60))), (37 + (19.7 / 60), -(89 + (46.6 / 60))),
            (37 + (53.1 / 60), -(88 + (52.8 / 60))), (38 + (26.3 / 60), -(87 + (57.0 / 60))),
            (38 + (59.5 / 60), -(86 + (59.1 / 60))), (39 + (32.6 / 60), -(85 + (58.9 / 60))),
            (40 + (5.6 / 60), -(84 + (56.3 / 60))), (40 + (38.4 / 60), -(83 + (51.1 / 60))),
            (41 + (11.0 / 60), -(82 + (43.0 / 60))), (41 + (43.5 / 60), -(81 + (31.9 / 60))),
            (42 + (15.8 / 60), -(80 + (17.4 / 60))), (42 + (47.8 / 60), -(78 + (59.2 / 60))),
            (43 + (19.5 / 60), -(77 + (37.0 / 60))), (43 + (50.9 / 60), -(76 + (10.5 / 60))),
            (44 + (21.9 / 60), -(74 + (39.1 / 60))), (44 + (52.4 / 60), -(73 + (2.4 / 60))),
            (45 + (22.4 / 60), -(71 + (19.7 / 60))), (45 + (51.8 / 60), -(69 + (30.3 / 60))),
            (46 + (20.5 / 60), -(67 + (33.4 / 60))), (46 + (48.2 / 60), -(65 + (27.8 / 60))),
            (47 + (14.8 / 60), -(63 + (12.1 / 60))), (47 + (40.1 / 60), -(60 + (44.7 / 60))),
            (48 + (3.7 / 60), -(58 + (3.1 / 60))), (48 + (25.1 / 60), -(55 + (3.9 / 60))),
            (48 + (43.7 / 60), -(51 + (42.4 / 60))), (48 + (58.2 / 60), -(47 + (50.4 / 60))),
            (49 + (6.6 / 60), -(43 + (13.1 / 60))), (49 + (3.9 / 60), -(37 + (15.7 / 60)))    
        ]
        
        
        folium.PolyLine(locations=coordinates_sur, color='black').add_to(mexico_map)
        folium.PolyLine(locations=coordinates_norte, color='black').add_to(mexico_map)
        folium.PolyLine(locations=coordinates_centro, color='red').add_to(mexico_map)

        from geopy.distance import geodesic

        def calculate_new_coordinates(coord, bearing, distance):
            # Calcula las nuevas coordenadas dados el rumbo (bearing) y la distancia
            # El bearing se mide en grados, donde 0 es hacia el norte, 90 es hacia el este, etc.
            new_coord = geodesic(kilometers=distance).destination(coord, bearing)
            return new_coord.latitude, new_coord.longitude

        def expand_coordinates_north(coordinates, distance_increase):
            # Expande las coordenadas hacia el norte

            expanded_coordinates = [coordinates[0]]
            for coord in coordinates:
                new_coord = calculate_new_coordinates(coord, 0, 1.15*distance_increase)
                expanded_coordinates.append(new_coord)

            return expanded_coordinates

        def expand_coordinates_south(coordinates, distance_increase):
            # Expande las coordenadas hacia el sur

            expanded_coordinates = [coordinates[-1]]
            for coord in reversed(coordinates):
                new_coord = calculate_new_coordinates(coord, 180, distance_increase)
                expanded_coordinates.append(new_coord)

            return expanded_coordinates[1:]

        # Definir la distancia adicional que deseas agregar a la anchura
        #distance_increase = 900  # en kilómetros
        # Definir la distancia adicional que deseas agregar a la anchura
        distance_increase = st.sidebar.slider("Aumento de distancia (km)", min_value=0, max_value=3000, value=200, step=100)

        # Expande las coordenadas del borde norte
        expanded_coordinates_norte = expand_coordinates_north(coordinates_sur, distance_increase)

        # Expande las coordenadas del borde sur    
        expanded_coordinates_sur = expand_coordinates_south(coordinates_norte, distance_increase) 

        # Mostrar el mapa#
        #mexico_map = folium.Map(location=[23.6345, -102.5528], zoom_start=5)  # Ubicación central de México
        folium.PolyLine(locations=expanded_coordinates_norte, color='orange').add_to(mexico_map)
        folium.PolyLine(locations=expanded_coordinates_sur, color='orange').add_to(mexico_map)


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
