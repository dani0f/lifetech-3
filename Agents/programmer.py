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

example_human = """
slice:
title: FICHA TÉCNICA
subtitle: PROTOCOLO DE VIGILANCIA TRASTORNOS MUSCULOESQUELÉTICOS RELACIONADOS AL TRABAJO (TMERT)

slice:
title: ¿Qué es el Protocolo TMERT?
subtitle: Procedimiento y objetivos
text: Es un procedimiento que entrega directrices para la prevención y control de los trastornos musculoesqueléticos (TME) de las extremidades superiores en las 
empresas. Contempla la identificación y evaluaciones de factores de riesgo biomecánicos, organizacionales y psicosociales en los puestos de trabajo, además de la vigilancia a la salud de los trabajadores expuestos.

slice:
title: Normativa asociada
subtitle: Responsabilidades de la empresa
item: Evaluar los factores de riesgos detectados y aplicar un programa de control del riesgo.
item: Eliminar o mitigar los riesgos detectados y aplicar un programa de control del riesgo.
item: Informar a los trabajadores sobre los factores a los que están expuestos, las medidas preventivas y los métodos de trabajo correctos.
item: Cumplir con la Norma Técnica MINSAL TMERT de extremidades superiores y el Protocolo de Vigilancia para trabajadores expuestos a factores de riesgo de TMERT.

slice:
title: Fiscalización de las Mutualidades de Empleadores
enum: Superintendencia de Seguridad Social: www.suseso.cl.
enum: ACHS CENTER: Teléfono 600 600 22 47, página web www.achs.cl.

slice:
title: ¡Gracias por su atención!
text: Nombre del archivo: protocolos-ministerio-de-salud-trastornos-musculoesqueléticos-relacionados-al-trabajo-tmert.pdf"""

template = """Crea un div html con la idea propuesta basándote en el contexto de abajo para responder a la pregunta planteada. Si no puedes crearlo correctamente responde "No puedo hacerlo".

Contexto: Eres un desarrollador web profesional y estás trabajando en una página web para un cliente. Tu trabajo consiste utilizar las palabras que demarcan titulos (title), subtitulos (subtitle)
texto (text), itemizador (item) y enumarador (enum) para crear una presentación de diapositivas (slides) utilizando html y css. Se espera que devuelva
un div html para cada diapositiva de la presentación. Debe haber estilos en la mayoría de los elementos usando css incrustado
dentro del div html. La salida debe ser un arreglo de python donde cada div (slide) sea un elemento del arreglo slides"""

example_ai = """slides = [
    "<div class=\"slide\" style=\"display: flex; height: 100vh; align-items: stretch; justify-content: center; background-color: #00a19a; overflow-x: auto;\"><div class=\"column white\" style=\"flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center; justify-content: center;\"><div class=\"content\"><h1>FICHA TÉCNICA</h1><h2 style=\"color: #00a19a;\">PROTOCOLO DE VIGILANCIA TRASTORNOS MUSCULOESQUELÉTICOS RELACIONADOS AL TRABAJO (TMERT)</h2></div></div></div>",
    "<div class=\"slide\" style=\"display: flex; height: 100vh; align-items: stretch; justify-content: center; background-color: #00a19a; overflow-x: auto;\"><div class=\"column white\" style=\"flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center; justify-content: center;\"><div class=\"content\"><h1>¿Qué es el Protocolo TMERT?</h1><h2>Procedimiento y objetivos</h2><p>Es un procedimiento que entrega directrices para la prevención y control de los trastornos musculoesqueléticos (TME) de las extremidades superiores en las empresas. Contempla la identificación y evaluaciones de factores de riesgo biomecánicos, organizacionales y psicosociales en los puestos de trabajo, además de la vigilancia a la salud de los trabajadores expuestos.</p></div></div></div>",
    "<div class=\"slide\" style=\"display: flex; height: 100vh; align-items: stretch; justify-content: center; background-color: #00a19a; overflow-x: auto;\"><div class=\"column white\" style=\"flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center; justify-content: center;\"><div class=\"content\"><h1>Normativa asociada</h1><h2>Responsabilidades de la empresa</h2></div></div><div class=\"column\" style=\"flex: 1; padding: 2rem; color: #fff;\"><div class=\"content\"><h2>Responsabilidades de la empresa</h2><ul style=\"list-style-type: disc;\"><li>Evaluar los factores de riesgos detectados y aplicar un programa de control del riesgo.</li><li>Eliminar o mitigar los riesgos detectados y aplicar un programa de control del riesgo.</li><li>Informar a los trabajadores sobre los factores a los que están expuestos, las medidas preventivas y los métodos de trabajo correctos.</li><li>Cumplir con la Norma Técnica MINSAL TMERT de extremidades superiores y el Protocolo de Vigilancia para trabajadores expuestos a factores de riesgo de TMERT.</li></ul></div></div></div>",
    "<div class=\"slide\" style=\"display: flex; height: 100vh; align-items: stretch; justify-content: center; background-color: #00a19a; overflow-x: auto;\"><div class=\"column\" style=\"flex: 1; padding: 2rem; color: #fff;\"><div class=\"content\"><h1>Fiscalización de las Mutualidades de Empleadores</h1></div></div><div class=\"column white\" style=\"flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center; justify-content: center;\"><div class=\"content\"><ol><li>Superintendencia de Seguridad Social: <a href=\"http://www.suseso.cl\">www.suseso.cl</a></li><li>ACHS CENTER: Teléfono 600 600 22 47, página web <a href=\"http://www.achs.cl\">www.achs.cl</a></li></ol></div></div></div>",
    "<div class=\"slide\" style=\"display: flex; height: 100vh; align-items: stretch; justify-content: center; background-color: #00a19a; overflow-x: auto;\"><div class=\"column white\" style=\"flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center; justify-content: center;\"><div class=\"content\"><h1>¡Gracias por su atención!</h1><h2>Fuentes:</h2><div class=\"paragraphs\" style=\"display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;\"><div><p>fuente:</p></div><div><p>Nombre del archivo: protocolos-ministerio-de-salud-trastornos-musculoesqueléticos-relacionados-al-trabajo-tmert.pdf</p></div></div></div></div></div>"
]
"""





system_message_prompt = SystemMessagePromptTemplate.from_template(template)
example_human = HumanMessagePromptTemplate.from_template(example_human)
example_ai = AIMessagePromptTemplate.from_template(example_ai)
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)


chat = ChatOpenAI(openai_api_key=key, temperature=0.8, model="gpt-3.5-turbo")

chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, example_human, example_ai, human_message_prompt]
)
chain = LLMChain(llm=chat, prompt=chat_prompt)

ask = """slice:
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


result=chain.run(f"{ask}")
print(result)


