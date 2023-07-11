import streamlit as st
from Agents.programmer import askProgrammer
from Agents.summarizer import askSummarizer
from Agents.narrator import playNarrator, askNarrator
from search_engine.semantic_search import query
import pyttsx3
from search_engine.save_embeddings import load_embeddings
from search_engine.read_files import load_files
from search_engine.generate_files import generate_files
from search_engine.download_model import download_model
import os

# -- Set page config
apptitle = 'Life tech-3'

st.set_page_config(page_title=apptitle, page_icon="")

st.title('Life Tech-3')


#verificar si estan las carpetas

def required_paths():
  required_paths =["search_engine\model","search_engine\dataset"]
  if not os.path.isdir(required_paths[0]):
    print("Download model...")
    download_model()
  if not os.path.isdir(required_paths[1]):
    print("Save files...")
    generate_files()



@st.cache_data
def loadDocument():
  documents = load_files('search_engine\dataset')
  documents_embeddings = load_embeddings('search_engine\embeddings.csv')
  return documents, documents_embeddings

@st.cache_resource
def setEngine(rate):
  # Init and set properties
  engine = pyttsx3.init()
  voices = engine.getProperty('voices')  # Select the first voice in the list
  for v in voices:
      print(v,v.id)
  engine.setProperty('voice', voices[1].id)
  engine.setProperty('rate', rate) # Set the speaking rate in words per minute
  return engine


with st.spinner('Descargando archivos necesarios'): 
  required_paths()
  documents, document_embeddings = loadDocument()



# -- Create sidebar for plot controls
st.sidebar.markdown('## Configuración avanzada')

st.sidebar.markdown('#### Opciones de la presentación')


#---opciones avanzadas (al final)


velocity = st.sidebar.slider('Velocidad de reproducción', 0.75, 1.5, 1.0)  # min, max, default
velocity = velocity * 200


st.markdown("""
 * Realiza una consulta acerca de un instructivo
""")       

response = st.text_input('Consulta')


if response:
  with st.spinner('Cargando...'):
    engine = setEngine(150)
    search = query(response,documents,document_embeddings)
    print(search[:100])
    if(len(search) != 0 ):
      summarizer = askSummarizer(search)
      string_slides = askProgrammer(summarizer)
      string_narrations = askNarrator(string_slides)
      slides = string_slides.split("|")
      narrations = string_narrations.split("|")
      for s,n in zip(slides,narrations):
        component = st.components.v1.html(s, width=800, height=600)
        playNarrator(n, engine)
        component.empty()
    else:
      print("not found")

