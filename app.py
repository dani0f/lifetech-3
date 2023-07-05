import streamlit as st
import time
import generator
import os
import json 

# #Función que agrega el link con fontawesome
# def format_html(styled_html):
#   init_html = """<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">\n"""
#   end_html = ""  
#   return init_html + "".join(styled_html) + end_html

# #Función que recibe un string con html/css y lo convierte en un componente. Segundo input es el tiempo que se mostrara la diapositiva.



  

# st.divider()
# user_input = st.text_area("Pregunta", "¿Qué hago en caso de accidente?'")

def generate_diap(styled_html, show_time):    
  component = st.components.v1.html(styled_html, width=800, height=600)
  component
  time.sleep(show_time)
  component.empty()


# if os.path.exists("example.json"):
#   with open('example.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)

#   slides = []
#   for d in data.items():
#     div = ""
#     for _,s in  d[1].items():
#       div = div + s
#     slides.append(div)
#   print(slides[1])


#   for s in slides:
#     component = st.components.v1.html(s,800,800)
#     time.sleep(9)
#     component.empty()



# for diap in generator.diapositivas:
#   result = format_html(diap)
#   print(result)
#   component = st.components.v1.html(result, width=800, height=600)
#   time.sleep(9)
#   component.empty()
template_1 = """
<div class="slide" style="display: flex; height: 100vh; align-items: stretch; justify-content: center; background-color: #00a19a; overflow-x: auto;">
  <div class="column white" style="flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center; justify-content: center;">
      <div class="content">
          <h1>title</h1>
          <h2 style="color: #00a19a;">subtitle</h2>
          <p>texto</p>
            <ul>
              <li>item</li>
            </ul>
            <ol>
              <li>enum</li>
            </ol>          
      </div>
  </div>
</div>
"""

component = st.components.v1.html(template_1,800,600)


template_2 = """
<div class="slide" style="display: flex; height: 100vh; align-items: stretch; justify-content: center; background-color: #00a19a; overflow-x: auto;">
  <div class="column white" style="flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center; justify-content: center;">
      <div class="content">
          <h1>title</h1>
          <h2>subtitle</h2>
          <div class="paragraphs" style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                <p>text</p>
                <ul>
                  <li>item</li>
                </ul>
                  <p>text</p>
                <ol>
                  <li>enum</li>
                </ol>
          </div>
      </div>
  </div>
</div>
"""

component = st.components.v1.html(template_2,800,600)


template_3 = """
<div class="slide" style="display: flex; height: 100vh; align-items: stretch; justify-content: center; background-color: #00a19a; overflow-x: auto;">
  <div class="column white" style="flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center; justify-content: center;">
      <div class="content">
          <h1>title</h1>
          <h2>subtitle</h2>
      </div>
  </div>
    <div class="column" style="flex: 1; padding: 2rem; color: #fff;">
        <div class="content">
            <h2>subtitle</h2>
            <p>text</p>
            <ul>
              <li>item</li>
            </ul>
            <ol>
              <li>enum</li>
            </ol>
        </div>
    </div>
</div>
"""

component = st.components.v1.html(template_3,800,600)

template_4 = """
<div class="slide" style="display: flex; height: 100vh; align-items: stretch; justify-content: center; background-color: #00a19a; overflow-x: auto;">
  <div class="column" style="flex: 1; padding: 2rem; color: #fff;">
    <div class="content">
        <h1>subtitle</h1>
        <p>text</p>
        <ul>
          <li>item</li>
        </ul>
        <ol>
          <li>enum</li>
        </ol>
    </div>
  </div>
  <div class="column white" style="flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center; justify-content: center;">
      <div class="content">
          <h1>title</h1>
          <h2>subtitle</h2>
      </div>
  </div>
</div>
"""

component = st.components.v1.html(template_4,800,600)