import streamlit as st
import time
import generator
import os
import json 
from Agents.programmer import askProgrammer
from Agents.summarizer import askSummarizer
from Agents.narrator import playNarrator, askNarrator
from search_engine.semantic_search import query
# #Función que agrega el link con fontawesome
# def format_html(styled_html):
#   init_html = """<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">\n"""
#   end_html = ""  
#   return init_html + "".join(styled_html) + end_html

# #Función que recibe un string con html/css y lo convierte en un componente. Segundo input es el tiempo que se mostrara la diapositiva.


# -- Set page config
apptitle = 'Life tech-3'

st.set_page_config(page_title=apptitle, page_icon="")

st.title('Life Tech-3')


# -- Create sidebar for plot controls
st.sidebar.markdown('## Configuración avanzada')

st.sidebar.markdown('#### Opciones de la presentación')


#---opciones avanzadas (al final)
velocity = st.sidebar.slider('Velocidad de reproducción', 0.75, 1.5, 1.0)  # min, max, default
velocity = velocity * 200



st.markdown("""
 * Realiza una pregunta acerca de un instructivo
""")
            

respuesta = st.text_input('Pregunta', '')
st.write('', respuesta )



if respuesta:
  st.spinner("Loading")
  with st.spinner('Wait for it...'):
    search = query(respuesta)
    if(len(search) != 0 ):
      summarizer = askSummarizer(search[0])
      string_slides = askProgrammer(summarizer)
      string_narrations = askNarrator(string_slides)
      slides = string_slides.split("|")
      narrations = string_narrations.split("|")
      for s,n in zip(slides,narrations):
        component = st.components.v1.html(s, width=800, height=600)
        playNarrator(n,200)
        component.empty()
    else:
      print("not found")


