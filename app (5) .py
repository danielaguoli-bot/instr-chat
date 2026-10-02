import streamlit as st
import pandas as pd

# =========================================================
# CONFIGURACIÓN
# =========================================================

st.set_page_config(
    page_title="Mundo Musical",
    page_icon="🎵",
    layout="wide"
)

# =========================================================
# ESTILOS
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #f8f7ff;
    color: #29263d;
}

.titulo {
    font-size: 55px;
    font-weight: bold;
    color: #29263d;
    text-align: center;
    margin-top: 20px;
}

.titulo span {
    color: #7957d5;
}

.subtitulo {
    text-align: center;
    color: #7957d5;
    font-size: 18px;
    margin-bottom: 30px;
}

.tarjeta {
    background-color: white;
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.08);
    min-height: 300px;
    margin-bottom: 15px;
}

.icono {
    font-size: 65px;
    background-color: #eee9ff;
    border-radius: 50%;
    width: 120px;
    height: 120px;
    margin: auto;
    display: flex;
    align-items: center;
    justify-content: center;
}

.nombre {
    color: #7957d5;
    font-size: 25px;
    font-weight: bold;
    margin-top: 15px;
}

.descripcion {
    font-size: 15px;
    line-height: 1.6;
}

.caja-chat {
    background-color: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.08);
}

.footer {
    text-align: center;
    color: #29263d;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# PORTADA
# =========================================================

st.markdown(
    '<div class="titulo">🎵 Mundo <span>Musical</span></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitulo">DESCUBRE EL MUNDO DE LOS INSTRUMENTOS MUSICALES</div>',
    unsafe_allow_html=True
)

st.write(
    "Explora diferentes instrumentos, conoce sus características, "
    "descubre sus familias y aprende de una manera interactiva."
)

st.markdown("---")


# =========================================================
# MENÚ
# =========================================================

opcion = st.selectbox(
    "🎼 Selecciona una sección:",
    [
        "Inicio",
        "Explorar instrumentos",
        "Familias musicales",
        "Tabla de instrumentos",
        "Gráfico",
        "🤖 Chatbot musical"
    ]
)


# =========================================================
# INICIO
# =========================================================

if opcion == "Inicio":

    st.header("🎶 Bienvenido a Mundo Musical")

    st.write(
        "Los instrumentos musicales son objetos creados para producir "
        "sonidos y formar parte de diferentes expresiones musicales. "
        "En esta página podrás conocer algunos instrumentos y sus características."
    )

    st.subheader("🎼 Familias de instrumentos")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="tarjeta">
            <div class="icono">🎸</div>
            <div class="nombre">Cuerda</div>
            <p class="descripcion">
            Producen sonido mediante la vibración de una o varias cuerdas.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="tarjeta">
            <div class="icono">🎺</div>
            <div class="nombre">Viento</div>
            <p class="descripcion">
            Producen sonido mediante la vibración del aire.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="tarjeta">
            <div class="icono">🥁</div>
            <div class="nombre">Percusión</div>
            <p class="descripcion">
            Producen sonido al ser golpeados, sacudidos o frotados.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="tarjeta">
            <div class="icono">🎹</div>
            <div class="nombre">Teclado</div>
            <p class="descripcion">
            Utilizan teclas para producir diferentes sonidos.
            </p>
        </div>
        """, unsafe_allow_html=True)


# =========================================================
# EXPLORAR INSTRUMENTOS
# =========================================================

elif opcion == "Explorar instrumentos":

    st.header("🎼 Explora los instrumentos")

    st.write(
        "Selecciona el botón 'Ver más' para conocer información sobre cada instrumento."
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    # ---------------- GUITARRA ----------------

    with col1:

        st.markdown("""
        <div class="tarjeta">
            <div class="icono">🎸</div>
            <div class="nombre">Guitarra</div>
            <p class="descripcion">
            Instrumento de cuerda utilizado en diferentes estilos musicales.
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Ver más 🎸", key="boton_guitarra"):
            st.success(
                "🎸 Guitarra\n\n"
                "La guitarra es un instrumento de cuerda. "
                "Produce sonido mediante la vibración de sus cuerdas. "
                "Se utiliza en géneros como rock, pop, música clásica y otros."
            )

    # ---------------- VIOLÍN ----------------

    with col2:

        st.markdown("""
        <div class="tarjeta">
            <div class="icono">🎻</div>
            <div class="nombre">Violín</div>
            <p class="descripcion">
            Instrumento de cuerda conocido por su sonido expresivo.
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Ver más 🎻", key="boton_violin"):
            st.success(
                "🎻 Violín\n\n"
                "El violín pertenece a la familia de cuerda. "
                "Normalmente se toca utilizando un arco que hace vibrar "
                "sus cuerdas."
            )

    st.write("")

    col3, col4 = st.columns(2)

    # ---------------- PIANO ----------------

    with col3:

        st.markdown("""
        <div class="tarjeta">
            <div class="icono">🎹</div>
            <div class="nombre">Piano</div>
            <p class="descripcion">
            Instrumento de teclado utilizado en numerosos géneros musicales.
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Ver más 🎹", key="boton_piano"):
            st.success(
                "🎹 Piano\n\n"
                "El piano es un instrumento de teclado. "
                "Al presionar sus teclas se activa un mecanismo "
                "que hace vibrar sus cuerdas y produce el sonido."
            )

    # ---------------- SAXOFÓN ----------------

    with col4:

        st.markdown("""
        <div class="tarjeta">
            <div class="icono">🎷</div>
            <div class="nombre">Saxofón</div>
            <p class="descripcion">
            Instrumento de viento utilizado en diferentes estilos musicales.
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Ver más 🎷", key="boton_saxofon"):
            st.success(
                "🎷 Saxofón\n\n"
                "El saxofón pertenece a los instrumentos de viento. "
                "Produce sonido cuando el aire hace vibrar una lengüeta "
                "ubicada en la boquilla."
            )


# =========================================================
# FAMILIAS MUSICALES
# =========================================================

elif opcion == "Familias musicales":

    st.header("🎶 Familias de instrumentos")

    st.write(
        "Selecciona una familia para conocer sus características."
    )

    familia = st.selectbox(
        "🎼 Selecciona una familia:",
        [
            "Cuerda",
            "Viento",
            "Percusión",
            "Teclado"
        ]
    )

    if familia == "Cuerda":

        st.subheader("🎸 Instrumentos de cuerda")

        st.write(
            "Producen sonido mediante la vibración de una o varias cuerdas."
        )

        st.info("🎸 Guitarra")
        st.info("🎻 Violín")
        st.info("🎼 Arpa")

    elif familia == "Viento":

        st.subheader("🎺 Instrumentos de viento")

        st.write(
            "Producen sonido mediante la vibración del aire."
        )

        st.info("🎺 Trompeta")
        st.info("🎷 Saxofón")
        st.info("🪈 Flauta")

    elif familia == "Percusión":

        st.subheader("🥁 Instrumentos de percusión")

        st.write(
            "Producen sonido principalmente al ser golpeados, "
            "sacudidos o frotados."
        )

        st.info("🥁 Batería")
        st.info("🪘 Tambor")
        st.info("🎵 Maracas")

    elif familia == "Teclado":

        st.subheader("🎹 Instrumentos de teclado")

        st.write(
            "Utilizan teclas para producir diferentes sonidos."
        )

        st.info("🎹 Piano")
        st.info("🎹 Órgano")
        st.info("🎹 Teclado electrónico")


# =========================================================
# TABLA
# =========================================================

elif opcion == "Tabla de instrumentos":

    st.header("📋 Tabla de instrumentos")

    st.write(
        "Esta tabla muestra algunos instrumentos y la familia a la que pertenecen."
    )

    datos = {
        "Instrumento": [
            "Guitarra",
            "Violín",
            "Arpa",
            "Trompeta",
            "Saxofón",
            "Flauta",
            "Batería",
            "Tambor",
            "Maracas",
            "Piano",
            "Órgano",
            "Teclado electrónico"
        ],

        "Familia": [
            "Cuerda",
            "Cuerda",
            "Cuerda",
            "Viento",
            "Viento",
            "Viento",
            "Percusión",
            "Percusión",
            "Percusión",
            "Teclado",
            "Teclado",
            "Teclado"
        ]
    }

    tabla = pd.DataFrame(datos)

    st.dataframe(
        tabla,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# GRÁFICO
# =========================================================

elif opcion == "Gráfico":

    st.header("📊 Instrumentos por familia")

    st.write(
        "El gráfico muestra la cantidad de instrumentos registrados "
        "en cada familia musical."
    )

    datos_grafico = {
        "Familia": [
            "Cuerda",
            "Viento",
            "Percusión",
            "Teclado"
        ],

        "Cantidad": [
            3,
            3,
            3,
            3
        ]
    }

    grafico = pd.DataFrame(datos_grafico)

    st.bar_chart(
        grafico.set_index("Familia")
    )

    st.subheader("📌 Datos del gráfico")

    st.write("🎸 Cuerda: 3 instrumentos")
    st.write("🎺 Viento: 3 instrumentos")
    st.write("🥁 Percusión: 3 instrumentos")
    st.write("🎹 Teclado: 3 instrumentos")


# =========================================================
# CHATBOT
# =========================================================

elif opcion == "🤖 Chatbot musical":

    st.header("🤖 Chatbot musical")

    st.write(
        "Hola 👋 Soy el asistente de Mundo Musical. "
        "Escribe una pregunta sobre instrumentos o familias musicales."
    )

    st.markdown("---")

    pregunta = st.text_input(
        "💬 Escribe tu pregunta:",
        placeholder="Ejemplo: ¿Qué es una guitarra?"
    )

    if pregunta:

        texto = pregunta.lower()

        if "guitarra" in texto:

            respuesta = (
                "🎸 La guitarra es un instrumento de cuerda. "
                "Produce sonido mediante la vibración de sus cuerdas "
                "y se utiliza en diferentes géneros musicales."
            )

        elif "violín" in texto or "violin" in texto:

            respuesta = (
                "🎻 El violín es un instrumento de cuerda. "
                "Normalmente se toca utilizando un arco que hace vibrar "
                "sus cuerdas."
            )

        elif "piano" in texto:

            respuesta = (
                "🎹 El piano es un instrumento de teclado. "
                "Al presionar sus teclas se activa un mecanismo que "
                "hace vibrar sus cuerdas y produce sonido."
            )

        elif "saxofón" in texto or "saxofon" in texto:

            respuesta = (
                "🎷 El saxofón es un instrumento de viento. "
                "Produce sonido cuando el aire hace vibrar una lengüeta "
                "ubicada en la boquilla."
            )

        elif "cuerda" in texto:

            respuesta = (
                "🎸 Los instrumentos de cuerda producen sonido mediante "
                "la vibración de una o varias cuerdas. "
                "Ejemplos: guitarra, violín y arpa."
            )

        elif "viento" in texto:

            respuesta = (
                "🎺 Los instrumentos de viento producen sonido mediante "
                "la vibración del aire. "
                "Ejemplos: trompeta, saxofón y flauta."
            )

        elif "percusión" in texto or "percusion" in texto:

            respuesta = (
                "🥁 Los instrumentos de percusión producen sonido "
                "principalmente al ser golpeados, sacudidos o frotados. "
                "Ejemplos: batería, tambor y maracas."
            )

        elif "teclado" in texto:

            respuesta = (
                "🎹 Los instrumentos de teclado utilizan teclas para "
                "producir diferentes sonidos. "
                "Ejemplos: piano, órgano y teclado electrónico."
            )

        elif "familia" in texto:

            respuesta = (
                "🎼 En esta página trabajamos cuatro familias: "
                "cuerda, viento, percusión y teclado."
            )

        elif "hola" in texto or "buenas" in texto:

            respuesta = (
                "👋 ¡Hola! Soy el chatbot de Mundo Musical. "
                "Pregúntame sobre guitarra, violín, piano, saxofón "
                "o las familias musicales."
            )

        else:

            respuesta = (
                "🤔 No encontré una respuesta para esa pregunta. "
                "Puedes preguntarme sobre guitarra, violín, piano, "
                "saxofón, cuerda, viento, percusión o teclado."
            )

        st.success("🤖 " + respuesta)


# =========================================================
# PIE DE PÁGINA
# =========================================================

st.markdown("---")

st.markdown(
    """
    <div class="footer">
        🎵 <b>Mundo Musical</b><br>
        Proyecto desarrollado con Python y Streamlit
    </div>
    """,
    unsafe_allow_html=True
)

    