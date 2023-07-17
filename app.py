import streamlit as st
from Agents.programmer import askProgrammer
from Agents.summarizer import askSummarizer
from Agents.narrator import playNarrator, askNarrator
from search_engine.semantic_search import query
from search_engine.save_embeddings import load_embeddings
from search_engine.read_files import load_files
from search_engine.generate_files import generate_files
from search_engine.download_model import download_model
from Audio.generate_audio import generate_audios, play_audio
import os
import base64
from mutagen.mp3 import MP3
import time


# -- Set page config
apptitle = 'Life tech-3'

st.set_page_config(page_title=apptitle, page_icon="")


st.title('Life:green[Tech] :male-doctor:')

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



def autoplay_audio(file_path: str):
  with open(file_path, "rb") as f:
    data = f.read()
    b64 = base64.b64encode(data).decode()
    md = f"""
        <audio autoplay="true">
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
    markdown_placeholder = st.empty()  # Crear un espacio en blanco para el markdown
    markdown_placeholder.markdown(
        md,
        unsafe_allow_html=True,
    )
  audio = MP3(file_path)
  length = audio.info.length
  time.sleep(length)
  markdown_placeholder.empty()  # Eliminar el contenido del espacio en blanco


  

with st.spinner('Descargando archivos necesarios'): 
  required_paths()
  documents, document_embeddings = loadDocument()


response = st.text_input("""
Realiza una consulta acerca de un **instructivo**
""",placeholder="¿Qué hago en caso de un tsunami?")

styles = """<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" integrity="sha512-iecdLmaskl7CVkqkXNQ/ZH/XLlvWZOJyj7Yy7tcenmpD1ypASozpmT/E0iPtmFIB46ZmdtAc9eNBvH0H/ZpiBw==" crossorigin="anonymous" referrerpolicy="no-referrer" />

<style>
  body {
    margin: 0;
    padding: 0;
    font-family: 'Arial', sans-serif;
  }

  .slide {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    max-width: 100vw;
    padding: 2rem;
    box-sizing: border-box;
    background-color: #fff;
  }

  .slide h1 {
    font-size: 2.0rem;
    margin-bottom: 1.5rem;
    color: #00a19a;
    font-weight: bold;
    text-transform: uppercase;
  }

  .slide h2 {
    font-size: 1.5rem;
    margin-bottom: 1.2rem;
    color: #333;
  }

  .slide p {
    font-size: 1.2rem;
    margin-bottom: 0.8rem;
    color: #555;
  }

  .slide ul {
    margin-top: 0;
    margin-bottom: 1.5rem;
    padding-left: 2rem;
    color: #555;
    font-size: 1.2rem;
  }

  .slide li {
    margin-bottom: 0.5rem;
  }

  .slide a {
    color: #0000FF;
    text-decoration: none;
  }

  .slide a:hover {
    text-decoration: underline;
  }

  .slide i {
    font-size: 2.5rem;
    color: #00a19a;
  }
</style>"""


search = ""
if response:
  with st.spinner('Cargando...'):
    search = query(response,documents,document_embeddings)
    print("search",search)
    if(len(search) > 0 ):
      #print(search[:50])
      #summarizer 
      string_slides = askSummarizer(search)
      string_narrations = askNarrator(string_slides)
      narrations = string_narrations.split("|")  
      audios = generate_audios(narrations)  

      slides = ["""<div class="slide">""" + slide for slide in string_slides.split("""<div class="slide">""")[1:]]




  if(len(search) > 0):
    print("SEARCH ",search)
    progress_bar = st.progress(0)
    for i, audio_filename in enumerate(audios):
      #print(slides[i])
      #print(narrations[i])
      component = st.components.v1.html(slides[i] + styles, width=700, height=600)  
      duration = autoplay_audio(audio_filename)
      progress = (i + 1) / len(audios)
      progress_bar.progress(progress)
      component.empty()
    progress_bar.empty()

  else:
    print("not found")
    st.write("Not found")






