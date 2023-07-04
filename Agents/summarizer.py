from langchain.chat_models import ChatOpenAI
import json
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import AIMessage, HumanMessage, SystemMessage

with open("credentials.json", "r") as f:
    api = json.load(f)
    key = api["openai"]


example_human = """Nombre archivo: protocolos-ministerio-de-salud-maneja-manual-de-carga.pdf
FICHA
TÉCNICA
PROTOCOLO DE MANEJO DE MANUAL DE CARGA (MMC)
¿QUÉ ES EL PROTOCOLO DE MANEJO
DE MANUAL DE CARGA (MMC)?
Es una guía o procedimiento diseñado por ACHS (basado en la Guía Técnica MMC/2018)
para realizar la gestión preventiva de los riesgos a la salud o a las condiciones de los
trabajadores derivados del manejo o manipulación manual de carga de sus puestos de
trabajo, señalándose en él los criterios y recomendaciones que orientan el cumplimiento
del las exigencias de la Ley 20.001, Ley 20.949 y del D.S Nº63/2005 del Ministerio del
Trabajo y Previsión Social
"""
template = """Eres un escritor y organizador de texto experto. Tu trabajo es tomar un texto plano de un instructivo, 
resumir las partes importantes y convertirlo en una presentación de diapositivas debes utilizar la palabra "diapositiva" para demarcar el inicio de una nueva diapositiva, 
la palabra "Titulo" para denotar que el texto será el título, "subtitulo" para denotar un subtítulo, "texto" para denotar el texto de la diapositiva y "item" para denotar un itemizador o enumerador del texto"""

example_ai ="""
Diapositiva:
Titulo: Protocolo de manejo de manual de carga (MMC)
Subtitulo: ¿Qué es el protocolo de manejo de manual de carga (MMC)?
item: Es una guiá o procedimiento diseñado por ACHS (basado en la Guía Técnica MMC/2018).
item: Sirve para realizar la gestión preventiva de riesgos a la salud o a las condiciones del manejo o manipulación de carga de sus puestoos de trabajo.
item: En el se señala los criterios y recomendaciones que orientan el complimiento de las exigencias de la Ley 20.001, Ley 20.949 y del D.S Nº63/2005 del Ministerio del
Trabajo y Previsión Social.

Diapositiva: 
Titulo: ¡Gracias por su atención!
"""

system_message_prompt = SystemMessagePromptTemplate.from_template(template)
example_human = HumanMessagePromptTemplate.from_template(example_human)
example_ai = AIMessagePromptTemplate.from_template(example_ai)
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)


chat = ChatOpenAI(openai_api_key=key, temperature=0.8, model="gpt-3.5-turbo")
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)


ask = """Nombre archivo: programa-de-asistencia-al-cumplimiento.pdf
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



messages = [
    SystemMessage(content="""Eres un escritor y organizador de texto experto. Tu trabajo es tomar un texto plano de un instructivo, resumir las partes importantes y convertirlo en una presentación de diapositivas debes utilizar la palabra "diapositiva" para demarcar el inicio de una nueva diapositiva, la palabra "Titulo" para denotar que el texto será el título, "subtitulo" para denotar un subtítulo, "texto" para denotar el texto de la diapositiva y "*" para denotar un itemice o enumerate del texto"""),
    HumanMessage(content=ask)
]

chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, example_human, example_ai, human_message_prompt]
)
chain = LLMChain(llm=chat, prompt=chat_prompt)
# get a chat completion from the formatted messages
result=chain.run("""Nombre archivo: protocolos-ministerio-de-salud-plan-nacional-de-erradicacion-de-la-ssilicosis-planes.pdf
FICHA
TÉCNICA
PLAN NACIONAL DE ERRADICACIÓN DE LA SILICOSIS (PLANESI)
¿ QUÉ ES EL PLANESI?
Es el Plan Nacional de Erradicación de la Silicosis, promulgado por el Ministerio del
Trabajo y Ministerio de Salud el 13 de Julio de 2007. Sus objetivos estratégicos incluyen
la disminución y control de la exposición a sílice en los lugares de trabajo, disminuir
progresivamente la generación de silicosis y fortalecer la vigilancia ambiental y de la
salud de los trabajadores expuestos.
NORMATIVA
¿QUÉ RESPONSABILIDAD TIENE LA EMPRESA?
ASOCIADA
• Informar a sus trabajadores de los riesgos de la sílice, medidas preventivas y métodos de
trabajo • El “Protocolo de Vigilancia del Ambiente de
Trabajo y de la Salud de los Trabajadores con
• Implementar un Sistema de Gestión de Seguridad y Salud en el Trabajo (SGSST) de acuerdo
a las directrices de la OIT Exposición a Sílice” comenzó a regir a partir del
03 de junio del 2015, mediante la Resolución
• Implementar medidas necesarias de seguridad y de protección de la salud de los
trabajadores Exenta N° 268/2015
• Proporcionar a sus trabajadores elementos de protección personal
• D.S N° 594 del Ministerio de Salud
• D.S N°18, Art 3 del Ministerio de Salud
• Guía para La Selección y Control de Protección
Respiratoria, Resolución 1391/2007 ISP
Las Mutualidades de Empleadores son fiscalizadas por la Superintendencia de Seguridad Social (www.suseso.cl) ACHS CENTER 600 600 22 47 - www.achs.cl """)

print(result)


