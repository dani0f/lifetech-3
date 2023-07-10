import streamlit as st
import time
import generator
import os
import json
from Agents.programmer import askProgrammer
from Agents.summarizer import askSummarizer
from Agents.narrator import playNarrator, askNarrator
from search_engine.semantic_search import query

# -- Set page config
apptitle = 'Life tech-3'
st.set_page_config(page_title=apptitle, page_icon="馃憮")

st.title('Life Tech-3')

# -- Create a text element and let the reader know the data is loading.
strain_load_state = st.text('Loading data...this may take a minute')

# -- Create sidebar for plot controls
st.sidebar.markdown('## Configuración avanzada')
st.sidebar.markdown('#### Opciones de la presentación')

# ---opciones avanzadas (al final)
dtboth = st.sidebar.slider('Velocidad de reproducción', 0.1, 5.0, 2.0)  # min, max, default
rate = int(dtboth * 100)

whiten = st.sidebar.checkbox('Musica', value=True)

st.markdown("""
 * Realiza una pregunta acerca de un instructivo
""")

respuesta = st.text_input('Pregunta', '')
st.write('', respuesta)

def skip():
    component.empty()
    next_placeholder.empty()

if respuesta:
    search = query(respuesta)
    if len(search) != 0:
        summarizer = askSummarizer(search[0])
        slides = askProgrammer(summarizer)
        for diap in slides:
            print("DIAP: ", diap)
            if diap == "":
                continue
            narrator = askNarrator(diap)
            print("NARRADOR:", narrator)
            component = st.components.v1.html(diap, width=800, height=600)
            duration = playNarrator(narrator, rate)
            audio_file = open("narration.wav", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/wav", start_time=0)
            next_placeholder = st.empty()
            next_placeholder.button("Siguiente diapositiva", on_click=skip, key='next')
            time.sleep(duration + 3)
            continue
        respuesta = ""
        st.markdown("### Fin de la presentación, esperamos que haya sido útil!")
    else:
        print("not found")
