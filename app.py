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


# st.divider()
# user_input = st.text_area("Pregunta", "¿Qué hago en caso de accidente?'")


askP = """slice:
title: PROGRAMA DE ASISTENCIA AL CUMPLIMIENTO (PAC)

slice:
title: ¿A quién está dirigido?
text: Este programa está dirigido a empresas que tengan un máximo de 49 trabajadores contratados al momento de la infracción y que no hayan utilizado este beneficio en los últimos 12 meses.

slice:
title: ¿En qué situaciones puedo solicitar PAC?
item: La empresa ha sido notificada de una multa por normas de higiene y seguridad.
item: La empresa no ha solicitado la reconsideración de la multa.
item: La empresa ha corregido las infracciones sancionadas.
item: Las infracciones están relacionadas con normas de higiene y seguridad.
item: No se han interpuesto recursos judiciales contra la multa.

slice:
title: ¿Qué documentos necesito para el trámite?
item: Antecedentes que demuestren el cumplimiento de todas las disposiciones legales por las que se cursó la multa.
item: Solicitud de recursos administrativos (formulario F10).
item: Declaración jurada para recursos administrativos.

slice:
title: ¿Dónde y cómo hacer el trámite?
text: El trámite se realiza en las oficinas de la Inspección del Trabajo que cursó las infracciones. Siga estos pasos:
item: Reúna los antecedentes requeridos.
item: Vaya a la oficina de la Inspección del Trabajo correspondiente al domicilio de su empresa.
item: Explique el motivo de su visita y solicite la sustitución de multas por el programa de asistencia al cumplimiento.
item: Entregue los antecedentes requeridos.
item: Espere la respuesta en un plazo de 20 días hábiles, que puede llegar por carta certificada o visita de un funcionario de la Inspección del Trabajo.

slice:
title: Consecuencias de no corregir las infracciones
text: Si los empleadores no corrigen las infracciones que generaron la multa, no implementan el sistema de gestión de seguridad en el trabajo o no acreditan en forma oportuna, el monto de la multa aumentará en un 25%.

slice:
title: ¡Gracias por su atención!
text: Nombre del archivo: programa-de-asistencia-al-cumplimiento.pdf"""

askS = """Nombre archivo: programa-de-asistencia-al-cumplimiento.pdf
    PROGRAMA DE ASISTENCIA AL CUMPLIMIENTO
    (PAC)
    Permite a las empresas solicitar la sustitución de una multa asociada a las normas de higiene y seguridad, por la incorporación al
    Programa de Asistencia al Cumplimiento (PAC).
    ¿A quién está dirigido?
    Empresas que tenga como máximo 49 trabajadores contratados al momento de constatarse la infracción, incluyendo las
    sucursales o establecimientos regionales.
    Y que no han hecho uso de este beneficio dentro de los 12 meses contados desde que se resolvió la solicitud de sustitución
    anterior.
    ¿En qué situaciones puedo solicitar PAC?
    ·
    La empresa ha sido notificada de la aplicación de la multa, por medio de una resolución.
    ·
    La empresa no ha solicitado la reconsideración de la multa.
    ·
    La empresa ha corregido las infracciones sancionadas.
    ·
    Las infracciones en las que incurrieron estén relacionadas a las normas de higiene y seguridad.
    ·
    No han interpuesto recursos judiciales contra la misma resolución.
    ¿Qué documentos necesito para hacer el trámite?
    ·Antecedentes que acrediten que la empresa dio cumplimiento íntegro a todas y cada una de las disposiciones legales por las que
    se cursó la multa.
    ·Solicitud de recursos administrativos. (formulario F10)
    ·Declaración jurada para recursos administrativos.
    ¿Dónde hago el trámite?
    En las oficinas de la DT que curso las infracciones
    ¿Cómo hago el trámite?
    1. Reúna los antecedentes requeridos (evidencia que subsano las infracciones).
    2.Diríjase a la oficina de la Inspección del Trabajo correspondiente al domicilio de la empresa.
    3.Explique el motivo de su visita: solicitar la sustitución de multas de higiene y seguridad por el programa de asistencia al
    cumplimiento.
    4.Entregue los antecedentes requeridos. (F10, Declaración jurada para recursos administrativos y evidencia que subsano las
    infracciones)
    5.Como resultado del trámite, habrá solicitado la sustitución de multas de higiene y seguridad, respuesta que podrá obtener en un
    plazo de 20 días hábiles, a través de una carta certificada o por la visita de un funcionario de la Inspección del Trabajo.
    Los empleadores que no corrijan las infracciones que dieron origen a la multa, no implementen el sistema de gestión de seguridad
    en el trabajo, o no efectúen la acreditación en forma oportuna, verán aumentado el monto original de la multa en un 25%."""


search = query("Incendios")

if(len(search) != 0 ):
  summarizer = askSummarizer(search[0])
  slides = askProgrammer(summarizer)
  for diap in slides:
    component = st.components.v1.html(diap, width=800, height=600)
    #component.empty()
else:
  print("not found")