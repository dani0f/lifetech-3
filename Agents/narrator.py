import pyttsx3
import subprocess
from pydub import AudioSegment
import os
import json
from langchain.chat_models import ChatOpenAI
from langchain import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)




def askNarrator(ask):

    with open("credentials.json", "r") as f:
        api = json.load(f)
        key = api["openai"]

    example_human = """slice:
title: Recomendaciones en caso de tsunami

slice:
title: Recomendaciones previas a un tsunami
text: - Infórmate sobre la zona de inundación por tsunami en tu comuna.
text: - Verifica si tu edificio se encuentra en una zona de fácil inundación.
text: - Identifica las vías de evacuación, puntos de encuentro y zonas sin riesgo de inundación.

slice:
title: Durante un tsunami
text: - Protégete durante un sismo violento: agáchate, cúbrete y afírmate.
text: - Evalúa si el terremoto ha causado daños y evacua si es necesario.
text: - Evacúa de inmediato si recibes una alerta oficial de tsunami o ves que el mar se retira.
text: - Dirígete a una zona libre de inundación a una altura de al menos 30 metros sobre el nivel del mar.
text: - Sigue las instrucciones de las autoridades y mantente en la zona segura hasta que sea seguro regresar.

slice:
title: Después de un tsunami
text: - Mantente alejado de los escombros en el agua.
text: - Regresa a tu hogar solo cuando las autoridades lo indiquen.
text: - Ingresa a tu vivienda con precaución y abre las ventanas para secar el lugar.
text: - Revisa el suministro de agua y alimentos, y hiérvela antes de beberla.
text: - Mantente informado a través de una radio o televisión a pilas.
text: - Utiliza el teléfono solo para emergencias y considera utilizar mensajes de texto.

slice:
title: Números de utilidad en caso de emergencia
text: - ACHS SAMU: Información sobre tipo de emergencia, estado de lesionados y dirección de la emergencia.
text: - ONEMI: Información sobre tipo de emergencia y dirección de la emergencia.

slice:
title: ¡Gracias por su atención!
text: Nombre del archivo: search_engine\documents/tsunami.pdf<Page:1>"""

    template = """Eres un amable presentador profesional de una mutual de seguridad.

    Tu trabajo consiste utilizar las palabras que demarcan diapositivas (slide), titulos (title), subtitulos (subtitle)
    texto (text), itemizador (item), enumarador (enum) y negrita (strong) para crear una narración de presentación de diapositivas (slides). Se espera que devuelvas
    una narración para cada diapositiva de la presentación.
    Las narraciones deben estar en formato csv delimitadas por el caracter barra vertical |.
    En caso de no existir contenido, ignora la narración de esa diapositiva.
    """

    example_ai = """Recomendaciones en caso de tsunami|
Infórmate sobre la zona de inundación por tsunami en tu comuna.
Verifica si tu edificio se encuentra en una zona de fácil inundación.
Identifica las vías de evacuación, puntos de encuentro y zonas sin riesgo de inundación.|
Durante un tsunami
Protégete durante un sismo violento: agáchate, cúbrete y afírmate.
Evalúa si el terremoto ha causado daños y evacua si es necesario.
Evacúa de inmediato si recibes una alerta oficial de tsunami o ves que el mar se retira.
Dirígete a una zona libre de inundación a una altura de al menos 30 metros sobre el nivel del mar.
Sigue las instrucciones de las autoridades y mantente en la zona segura hasta que sea seguro regresar.|
Después de un tsunami
Mantente alejado de los escombros en el agua.
Regresa a tu hogar solo cuando las autoridades lo indiquen.
Ingresa a tu vivienda con precaución y abre las ventanas para secar el lugar.
Revisa el suministro de agua y alimentos, y hiérvela antes de beberla.
Mantente informado a través de una radio o televisión a pilas.
Utiliza el teléfono solo para emergencias y considera utilizar mensajes de texto.|
Números de utilidad en caso de emergencia
ACHS SAMU: Información sobre tipo de emergencia, estado de lesionados y dirección de la emergencia.
ONEMI: Información sobre tipo de emergencia y dirección de la emergencia.|
¡Gracias por su atención!
Nombre del archivo: search_engine\documents/tsunami.pdf, Página 1.|
"""


    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    example_human = HumanMessagePromptTemplate.from_template(example_human)
    example_ai = AIMessagePromptTemplate.from_template(example_ai)
    human_template = "{text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)


    chat = ChatOpenAI(openai_api_key=key, temperature=0.2, model="gpt-3.5-turbo")

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, example_human, example_ai, human_message_prompt]
    )
    chain = LLMChain(llm=chat, prompt=chat_prompt)
    result = chain.run(ask)
    print(result)
    return result


def playNarrator(text, engine):
    # Step 2: Generate the narrator voice
    engine.save_to_file(text, 'narration.wav')
    engine.runAndWait()

    # Step 3: Get the duration of the audio file
    audio = AudioSegment.from_wav('narration.wav')
    duration = round(audio.duration_seconds, 1)
    print(f"Duration of the audio: {duration} seconds")

    # Step 4: Use ffmpeg to play the audio !!!!!!!!!!!!!!!
    # Requiere tener ffmpeg instalado en el sistema y anadido al PATH como variable de entorno
    # with para que no se muestre el output de ffplay en la consola y generemos logs de mas (Se puede quitar para debug)
    with open(os.devnull, 'w') as devnull:
        subprocess.call(['ffplay', '-nodisp', '-autoexit', 'narration.wav'], stdout=devnull, stderr=devnull)

    # Step 5: Delete the file audio after playing
    os.remove('narration.wav')
    return duration


