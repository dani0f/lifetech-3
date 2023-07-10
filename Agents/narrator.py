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

    example_human = """<div class="slide" style="display: flex; height: 100vh; align-items: stretch; justify-content: center; background-color: #00a19a; overflow-x: auto;"><div class="column white" style="flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center; justify-content: center;"><div class="content"><h1>Pasos sugeridos para la evacuación en caso de incendio</h1><ul style="list-style-type: disc;"><li>Si detecta una llama sin control o humo que indique un posible inicio de incendio, salga del lugar y avise inmediatamente a los trabajadores del área y jefatura disponible.</li><li>Si escucha la alarma o grito de advertencia de incendio, deje sus funciones y evacúe el lugar de trabajo hacia la zona de seguridad definida por la empresa.</li><li>Si hay visitas y/o clientes en la empresa, facilite su pronta evacuación. Hágalo con calma, no corra.</li><li>Llame a los Bomberos, indicando la dirección de la empresa, comuna, referencia de la ubicación y cualquier otra información que solicite la central de alarma.</li><li>Si existen lesionados, llame inmediatamente al número de emergencias de 
    la ACHS.</li><li>Corte el suministro eléctrico y de gas, siempre que esto no lo exponga al calor y humo emanado por el incendio. Informe de esta acción a la llegada de los Bomberos y oriéntelos respecto a la ubicación del foco de la emergencia.</li><li>Manténgase en la zona de seguridad a la espera de instrucciones de su jefatura y autoridades. Siempre considere estar alejado del calor y humo, facilitando también el acceso al personal de emergencia.</li><li>Se podrán retomar las labores e ingresar a las dependencias, sólo cuando la autoridad lo permita y la gerencia de la empresa lo indique.</li></ul></div></div></div>"""

    template = """Eres un amable presentador profesional de una mutual de seguridad.
    A partir de un html que simula ser una presentación de diapositivas deberás narrar el contenido.
    En caso de que el html no tenga contenido, ignora la narración de esa diapositiva.
    """

    example_ai = """Pasos sugeridos para la evacuación en caso de incendio
Si detecta una llama sin control o humo que indique un posible inicio de incendio, salga del lugar y avise inmediatamente a los trabajadores del área y jefatura disponible.
Si escucha la alarma o grito de advertencia de incendio, deje sus funciones y evacúe el lugar de trabajo hacia la zona de seguridad definida por la empresa.
Si hay visitas y/o clientes en la empresa, facilite su pronta evacuación. Hágalo con calma, no corra.
Llame a los Bomberos, indicando la dirección de la empresa, comuna, referencia de la ubicación y cualquier otra información que solicite la central de alarma.
Si existen lesionados, llame inmediatamente al número de emergencias de la ACHS.
Corte el suministro eléctrico y de gas, siempre que esto no lo exponga al calor y humo emanado por el incendio. Informe de esta acción a la llegada de los Bomberos y oriéntelos respecto a la ubicación del foco de la emergencia.
Manténgase en la zona de seguridad a la espera de instrucciones de su jefatura y autoridades. Siempre considere estar alejado del calor y humo, facilitando también el acceso al personal de emergencia.
Se podrán retomar las labores e ingresar a las dependencias, sólo cuando la autoridad lo permita y la gerencia de la empresa lo indique.
"""


    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    example_human = HumanMessagePromptTemplate.from_template(example_human)
    example_ai = AIMessagePromptTemplate.from_template(example_ai)
    human_template = "{text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)


    chat = ChatOpenAI(openai_api_key=key, temperature=0.5, model="gpt-3.5-turbo")

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, example_human, example_ai, human_message_prompt]
    )
    chain = LLMChain(llm=chat, prompt=chat_prompt)

    return chain.run(ask)




def playNarrator(text, rate=150):
    # Init and set properties
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')  # Select the first voice in the list
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', rate) # Set the speaking rate in words per minute
    engine.setProperty('volume', 0.7) # Set the volume between 0 and 1

    # Step 2: Generate the narrator voice
    engine.save_to_file(text, 'narration.wav')
    engine.runAndWait()

    # Step 3: Get the duration of the audio file
    audio = AudioSegment.from_wav('narration.wav')
    duration = round(audio.duration_seconds, 1)

    # Step 4: Use ffmpeg to play the audio !!!!!!!!!!!!!!!
    # Requiere tener ffmpeg instalado en el sistema y anadido al PATH como variable de entorno
    # with para que no se muestre el output de ffplay en la consola y generemos logs de mas (Se puede quitar para debug)
    return duration





