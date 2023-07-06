import streamlit as st
import time
import generator
import os
import json 
from Agents.programmer import askProgrammer
from Agents.summarizer import askSummarizer
from search_engine.semantic_search import query
# #Función que agrega el link con fontawesome
# def format_html(styled_html):
#   init_html = """<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">\n"""
#   end_html = ""  
#   return init_html + "".join(styled_html) + end_html

# #Función que recibe un string con html/css y lo convierte en un componente. Segundo input es el tiempo que se mostrara la diapositiva.


# -- Set page config
apptitle = 'Life tech-3'

st.set_page_config(page_title=apptitle, page_icon="馃憮")

st.title('Life Tech-3')

#with st.expander("Ver referencias"):

#    st.markdown("""
#Indica de donde se obtuvo la informaci贸n
#""")


#-- Create a text element and let the reader know the data is loading.
strain_load_state = st.text('Loading data...this may take a minute')
# -- Create sidebar for plot controls
st.sidebar.markdown('## Configuración avanzada')

st.sidebar.markdown('#### Opciones de la presentación')


#---opciones avanzadas (al final)
dtboth = st.sidebar.slider('Velocidad de reproducción', 0.1, 8.0, 1.0)  # min, max, default
dt = dtboth / 2.0

whiten = st.sidebar.checkbox('Musica', value=True)





st.markdown("""
 * Realiza una pregunta acerca de un instructivo
""")
            

respuesta = st.text_input('Pregunta', '')
st.write('', respuesta )

if respuesta:
  search = query(respuesta)
  if(len(search) != 0 ):
    summarizer = askSummarizer(search[0])
    slides = askProgrammer(summarizer)
    for diap in slides:
      component = st.components.v1.html(diap, width=800, height=600)
      #component.empty()
  else:
    print("not found")