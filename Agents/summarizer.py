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



def askSummarizer(ask):

    with open("credentials.json", "r") as f:
        api = json.load(f)
        key = api["openai"]


    example_human = """Nombre archivo: protocolos-ministerio-de-salud-hipobaria-intermitente-cronica-por-gran-altitud.pdf
    FICHA
    TÉCNICA
    GUÍA TÉCNICA SOBRE EXPOSICIÓN OCUPACIONAL A
    HIPOBARIA INTERMITENTE CRÓNICA POR GRAN ALTITUD
    El Ministerio de Salud en su constante tarea de velar por el cuidado de la Salud de la
    Población ha desarrollado la Guía Técnica sobre exposición ocupacional a H.I.C. por gran
    altitud.
    Esta guía tiene como objetivo principal la protección del trabajador que desempeñe labores
    sobre los 3000 msnm por mas de 6 meses, con una permanencia mínima de 30% de ese
    tiempo en sistemas de turnos rotativos a gran altitud y descanso a baja altitud.
    NORMATIVA
    ¿QUÉ RESPONSABILIDAD TIENE LA EMPRESA?
    ASOCIADA
    • Informar a sus trabajadores y trabajadoras sobre los riesgos de la Exposición. Impartir
    anualmente instrucción teórico-practica con una duración mínima de 3 Horas cronológicas, • DECRETO 28; modifica decreto N° 594, DE 1999,
    sobre el riesgo y las consecuencias para la salud Reglamento sobre condiciones sanitarias y
    • Contar con un Programa Preventivo realizado por Medico o Enfermera que debe constar ambientales básicas en los lugares de trabajo
    por escrito y actualizado cada año tendiente a preservar la salud de los Trabajadores
    • Guía técnica sobre exposición ocupacional a
    hipobaria intermitente crónica por gran altitud
    Las Mutualidades de Empleadores son fiscalizadas por la Superintendencia de Seguridad Social (www.suseso.cl) ACHS CENTER 600 600 22 47 - www.achs.cl
    """
    template = """Eres un escritor y organizador de texto experto. Tu trabajo es tomar un texto plano de un instructivo, 
    resumir las partes importantes y convertirlo en una presentación de diapositivas debes utilizar la palabra "slice" para demarcar el inicio de una nueva diapositiva, 
    la palabra "title" para denotar que el texto será el título, "subtitle" para denotar un subtítulo, "text" para denotar el texto de la diapositiva, "item" para denotar un itemizador y "enum" para denotar un enumerador del texto"""

    example_ai ="""
    slice:
    title: FICHA TÉCNICA
    subtitle: GUÍA TÉCNICA SOBRE EXPOSICIÓN OCUPACIONAL A HIPOBARIA INTERMITENTE CRÓNICA POR GRAN ALTITUD

    slice:
    title: Guía Técnica sobre exposición ocupacional a H.I.C. por gran altitud
    subtitle: Objetivo principal
    Esta guía tiene como objetivo principal la protección del trabajador que desempeñe labores
    sobre los 3000 msnm por mas de 6 meses, con una permanencia mínima de 30% de ese
    tiempo en sistemas de turnos rotativos a gran altitud y descanso a baja altitud.

    slice:
    title: Normativa asociada
    subtitle: Normativa y responsabilidades de la empresa
    text: Normativa: DECRETO 28 modifica decreto N° 594, de 1999, sobre el riesgo y las consecuencias para la salud Reglamento sobre condiciones sanitarias y ambientales básicas en los lugares de trabajo.
    text: Guía técnica sobre exposición ocupacional a hipobaria intermitente crónica por gran altitud

    Slice:
    title: ¿Qué responsabilidad tiene la empresa?
    item: Informar a los trabajadores sobre los riesgos de la exposición.
    item: Impartir instrucción teórico-práctica anual de al menos 3 horas cronológicas.
    item: Contar con un Programa Preventivo escrito y actualizado cada año.
    item: Seguir la Guía técnica sobre exposición ocupacional a hipobaria intermitente crónica por gran altitud.

    slice:
    title: Fiscalización de las Mutualidades de Empleadores:
    enum: Superintendencia de Seguridad Social: www.suseso.cl.
    enum: ACHS CENTER: Teléfono 600 600 22 47, página web www.achs.cl.
    slice:
    title: ¡Gracias por su atención!
    text: Nombre del archivo: protocolos-ministerio-de-salud-hipobaria-intermitente-cronica-por-gran-altitud.pdf 
    """

    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    example_human = HumanMessagePromptTemplate.from_template(example_human)
    example_ai = AIMessagePromptTemplate.from_template(example_ai)
    human_template = "{text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)


    chat = ChatOpenAI(openai_api_key=key, temperature=0.8, model="gpt-3.5-turbo")


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


    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, example_human, example_ai, human_message_prompt]
    )
    chain = LLMChain(llm=chat, prompt=chat_prompt)
    # get a chat completion from the formatted messages
    result=chain.run(ask)
    return(result)    



