import json
from langchain.chat_models import ChatOpenAI
from langchain import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


def askProgrammer(ask):
    with open("credentials.json", "r") as f:
        api = json.load(f)
        key = api["openai"]

    example_human = """
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
    enum: strong:Superintendencia de Seguridad Social: www.suseso.cl.
    enum: strong:ACHS CENTER: Teléfono 600 600 22 47, página web www.achs.cl.
    
    slice:
    title: ¡Gracias por su atención!
    text: strong:Nombre del archivo: 
    protocolos-ministerio-de-salud-hipobaria-intermitente-cronica-por-gran-altitud.pdf, Página: 1| """

    template = """Crea un div html con la idea propuesta basándote en el contexto de abajo para responder a la pregunta planteada. Si no puedes crearlo correctamente responde "No puedo hacerlo".

    Contexto: Eres un programador profesional y estás trabajando en una página web para un cliente. 
    Tu trabajo consiste utilizar las palabras que demarcan diapositivas (slide), titulos (title), subtitulos (subtitle)
    texto (text), itemizador (item), enumarador (enum) y negrita (strong) para crear una presentación de diapositivas (slides) utilizando html y css. Se espera que devuelvas
    un div html para cada diapositiva de la presentación. Cada uno de los slides resultantes deberás siempre terminarlo con el caracter barra vertical "|".
    
    Idea: utiliza siempre fondo blanco #fff, estilo de letra font-family: 'Arial', sans-serif;" y iconos de fontawesome centrados horizontalmente de tipo "solid" que coincidan con el contenido de la diapositiva."""
    
    example_ai = """<div class="slide" style="display: flex; height: 100vh; align-items: stretch; justify-content: center; overflow-x: auto; font-family: 'Arial', sans-serif; background-color: #fff;"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"><div class="column white" style="flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center; justify-content: center;"><div class="content" style="text-align: center;"><h1 style="color: #00a19a;">FICHA TÉCNICA</h1><h2>PROTOCOLO DE VIGILANCIA TRASTORNOS MUSCULOESQUELÉTICOS RELACIONADOS AL TRABAJO (TMERT)</h2><i class="fa-solid fa-x-ray" style="font-size: 5em; color: #00a19a;"></i><div style="display: flex; justify-content: center;"></div></div></div></div>|
    <div class="slide" style="display: flex; height: 100vh; align-items: stretch; justify-content: center; overflow-x: auto; background-color: #fff;"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"><div class="column white" style="flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center; justify-content: center;"><div class="content" style="font-family: 'Arial', sans-serif;"><h1 style="color: #00a19a; font-family: 'Helvetica Neue', Arial, sans-serif;">¿Qué es el Protocolo TMERT?</h1><h2>Procedimiento y objetivos</h2><i class="fa-solid fa-bullseye" style="font-size: 3em;"></i><p style="font-size: 1.2em; font-family: 'Arial', sans-serif;">Es un procedimiento que entrega directrices para la prevención y control de los trastornos musculoesqueléticos (TME) de las extremidades superiores en las empresas. Contempla la identificación y evaluaciones de factores de riesgo biomecánicos, organizacionales y psicosociales en los puestos de trabajo, además de la vigilancia a la salud de los trabajadores expuestos.</p></div></div></div>|
    <div class="slide" style="display: flex; height: 100vh; align-items: stretch; justify-content: center; overflow-x: auto; background-color: #fff; font-family: 'Arial', sans-serif;"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"><div class="column white" style="flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center;"><div class="content" style=""><i class="fa-regular fa-file" style="font-size: 3em; margin-left: 1em; margin-right: 1em;"></i><h1  style="color: #00a19a;">Normativa asociada</h1><h2>Responsabilidades de la empresa</h2><ul style="list-style-type: disc; text-align: left;"><li style="font-size: 1.2em;">Evaluar los factores de riesgos detectados y aplicar un programa de control del riesgo.</li><li style="font-size: 1.2em;">Eliminar o mitigar los riesgos detectados y aplicar un programa de control del riesgo.</li><li style="font-size: 1.2em;">Informar a los trabajadores sobre los factores a los que están expuestos, las medidas preventivas y los métodos de trabajo correctos.</li><li style="font-size: 1.2em;">Cumplir con la Norma Técnica MINSAL TMERT de extremidades superiores y el Protocolo de Vigilancia para trabajadores expuestos a factores de riesgo de TMERT.</li></ul></div></div></div>|
    <div class="slide" style="display: flex; height: 100vh; align-items: stretch; justify-content: center; overflow-x: auto; background-color: #fff; font-family: 'Arial', sans-serif;" ><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"><div class="column" style="flex: 1; padding: 2rem; display: flex; flex-direction: column; justify-content: center; align-items: center;"><div class="content"><h1 style="text-align: center; ">Fiscalización de las Mutualidades de Empleadores</h1><ol><li style="font-size: 1.2em;"><strong>Superintendencia de Seguridad Social:</strong> <a href="http://www.suseso.cl">www.suseso.cl</a></li><li style="font-size: 1.2em;"><strong>ACHS CENTER:</strong> Teléfono 600 600 22 47, página web <a href="http://www.achs.cl">www.achs.cl</a></li></ol></div></div></div></div></div>|
    <div class="slide" style="display: flex; height: 100vh; align-items: center; justify-content: center; background-color: #fff; font-family: 'Arial', sans-serif;"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"><div class="content" style="display: flex; flex-direction: column; align-items: center;"><h1 style="color: #00a19a; text-align: center;">¡Gracias por su atención!</h1><i class="fa-solid fa-circle-check" style="font-size: 2.2em; margin-top: 1rem;"></i><h2>Fuentes:</h2><ol><li style="font-size: 1.2em;"><strong>Nombre del archivo:</strong> protocolos-ministerio-de-salud-trastornos-musculoesqueléticos-relacionados-al-trabajo-tmert.pdf, página 1</li></ol></div></div>|"""
        
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    example_human = HumanMessagePromptTemplate.from_template(example_human)
    example_ai = AIMessagePromptTemplate.from_template(example_ai)
    human_template = "{text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)


    chat = ChatOpenAI(openai_api_key=key, temperature=0.3, model="gpt-3.5-turbo")

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, example_human, example_ai, human_message_prompt]
    )
    chain = LLMChain(llm=chat, prompt=chat_prompt)

    result = chain.run(ask)
    return result



