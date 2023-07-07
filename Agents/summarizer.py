import json
from langchain.chat_models import ChatOpenAI
from langchain import LLMChain
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
    resumir las partes importantes y convertirlo en una presentación de diapositivas, debes utilizar la palabra "slice" para demarcar el inicio de una nueva diapositiva, 
    la palabra "title" para denotar que el texto será el título, "subtitle" para denotar un subtítulo, "text" para denotar el texto de la diapositiva, "item" para denotar un itemizador, "enum" para denotar un enumerador del texto y 
    "strong" para resaltar una palabra utilizando negrita. El texto de cada diapositiva debe ser menor a 100 palabras y siempre debes terminar con una diapositiva de "gracias por su atención".
    """

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
    enum: strong:Superintendencia de Seguridad Social: 
    www.suseso.cl.
    enum: strong:ACHS CENTER: 
    Teléfono 600 600 22 47, página web www.achs.cl.

    slice:
    title: strong:¡Gracias por su atención!
    text: Nombre del archivo: 
    protocolos-ministerio-de-salud-hipobaria-intermitente-cronica-por-gran-altitud.pdf 
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
    # get a chat completion from the formatted messages
    return chain.run(ask)
 



