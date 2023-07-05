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




slides = [
    "<div class=\"slide\" style=\"display: flex; height: 100vh; align-items: stretch; justify-content: center; background-color: #00a19a; overflow-x: auto;\"><div class=\"column white\" style=\"flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center; justify-content: center;\"><div class=\"content\"><h1>PROGRAMA DE ASISTENCIA AL CUMPLIMIENTO (PAC)</h1></div></div></div>",
    "<div class=\"slide\" style=\"display: flex; height: 100vh; align-items: stretch; justify-content: center; background-color: #00a19a; overflow-x: auto;\"><div class=\"column white\" style=\"flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center; justify-content: center;\"><div class=\"content\"><h1>¿A quién está dirigido?</h1><p>Este programa está dirigido a empresas que tengan un máximo de 49 trabajadores contratados al momento de la infracción y que no hayan utilizado este beneficio en los últimos 12 meses.</p></div></div></div>",
    "<div class=\"slide\" style=\"display: flex; height: 100vh; align-items: stretch; justify-content: center; background-color: #00a19a; overflow-x: auto;\"><div class=\"column white\" style=\"flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center; justify-content: center;\"><div class=\"content\"><h1>¿En qué situaciones puedo solicitar PAC?</h1><ul><li>La empresa ha sido notificada de una multa por normas de higiene y seguridad.</li><li>La empresa no ha solicitado la reconsideración de la multa.</li><li>La empresa ha corregido las infracciones sancionadas.</li><li>Las infracciones están relacionadas con normas de higiene y seguridad.</li><li>No se han interpuesto recursos judiciales contra la multa.</li></ul></div></div></div>",
    "<div class=\"slide\" style=\"display: flex; height: 100vh; align-items: stretch; justify-content: center; background-color: #00a19a; overflow-x: auto;\"><div class=\"column white\" style=\"flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center; justify-content: center;\"><div class=\"content\"><h1>¿Qué documentos necesito para el trámite?</h1><ul><li>Antecedentes que demuestren el cumplimiento de todas las disposiciones legales por las que se cursó la multa.</li><li>Solicitud de recursos administrativos (formulario F10).</li><li>Declaración jurada para recursos administrativos.</li></ul></div></div></div>",
    "<div class=\"slide\" style=\"display: flex; height: 100vh; align-items: stretch; justify-content: center; background-color: #00a19a; overflow-x: auto;\"><div class=\"column\" style=\"flex: 1; padding: 2rem; color: #fff;\"><div class=\"content\"><h1>¿Dónde y cómo hacer el trámite?</h1><p>El trámite se realiza en las oficinas de la Inspección del Trabajo que cursó las infracciones. Siga estos pasos:</p><ol><li>Reúna los antecedentes requeridos.</li><li>Vaya a la oficina de la Inspección del Trabajo correspondiente al domicilio de su empresa.</li><li>Explique el motivo de su visita y solicite la sustitución de multas por el programa de asistencia al cumplimiento.</li><li>Entregue los antecedentes requeridos.</li><li>Espere la respuesta en un plazo de 20 días hábiles, que puede llegar por carta certificada o visita de un funcionario de la Inspección del Trabajo.</li></ol></div></div></div>",
    "<div class=\"slide\" style=\"display: flex; height: 100vh; align-items: stretch; justify-content: center; background-color: #00a19a; overflow-x: auto;\"><div class=\"column white\" style=\"flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center; justify-content: center;\"><div class=\"content\"><h1>Consecuencias de no corregir las infracciones</h1><p>Si los empleadores no corrigen las infracciones que generaron la multa, no implementan el sistema de gestión de seguridad en el trabajo o no acreditan en forma oportuna, el monto de la multa aumentará en un 25%.</p></div></div></div>",
    "<div class=\"slide\" style=\"display: flex; height: 100vh; align-items: stretch; justify-content: center; background-color: #00a19a; overflow-x: auto;\"><div class=\"column white\" style=\"flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center; justify-content: center;\"><div class=\"content\"><h1>¡Gracias por su atención!</h1><h2>Fuentes:</h2><div class=\"paragraphs\" style=\"display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;\"><div><p>fuente:</p></div><div><p>Nombre del archivo: programa-de-asistencia-al-cumplimiento.pdf</p></div></div></div></div></div>"
]


for diap in slides:
  component = st.components.v1.html(diap, width=800, height=600)
  time.sleep(3)
  component.empty()
