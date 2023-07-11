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

    example_human = """<div class="slide" style="display: flex; height: 100vh; align-items: stretch; justify-content: center; overflow-x: auto; font-family: 'Arial', sans-serif; background-color: #fff;"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"><div class="column white" style="flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center; justify-content: center;"><div class="content" style="text-align: center;"><h1 style="color: #00a19a;">Serie Procedimientos Emergencias - Qué hacer en caso de tsunami</h1><i class="fa-solid fa-wave-square" style="font-size: 5em; color: #00a19a;"></i><div style="display: flex; justify-content: center;"></div></div></div></div>|
<div class="slide" style="display: flex; height: 100vh; align-items: stretch; justify-content: center; overflow-x: auto; background-color: #fff;"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"><div class="column white" style="flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center; justify-content: center;"><div class="content" style="font-family: 'Arial', sans-serif;"><h1 style="color: #00a19a; font-family: 'Helvetica Neue', Arial, sans-serif;">Recomendaciones previas a un tsunami</h1><ul style="list-style-type: disc; text-align: left;"><li style="font-size: 1.2em;">Infórmate si la comuna de tu lugar de trabajo tiene identificada la zona de inundación por tsunami.</li><li style="font-size: 1.2em;">Revisa si el edificio en que trabajas se encuentra en una zona de fácil inundación.</li><li style="font-size: 1.2em;">Identifica las vías de evacuación, puntos de encuentro y la zona sin riesgo de inundación por tsunami.</li></ul></div></div></div>|
<div class="slide" style="display: flex; height: 100vh; align-items: stretch; justify-content: center; overflow-x: auto; background-color: #fff;"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"><div class="column white" style="flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center; justify-content: center;"><div class="content" style="font-family: 'Arial', sans-serif;"><h1 style="color: #00a19a; font-family: 'Helvetica Neue', Arial, sans-serif;">Durante un tsunami</h1><ul style="list-style-type: disc; text-align: left;"><li style="font-size: 1.2em;">Si estás en el borde costero y sientes un sismo violento, protégete con las tres reglas básicas: agáchate, cúbrete y afírmate.</li><li style="font-size: 1.2em;">Evalúa si el terremoto rompió murallas o dificultó que te mantuvieras en pie. En estos casos, debes evacuar de forma inmediata y no intentar salvar tus pertenencias.</li><li style="font-size: 1.2em;">Si recibes información oficial de alerta o alarma de tsunami, o ves que se recoge el mar, evacúa de inmediato a una zona libre de inundación a 30 metros de altura sobre el nivel del mar.</li><li style="font-size: 1.2em;">Quédate en la zona segura hasta que las autoridades indiquen que es seguro regresar a tu hogar. Las olas de un tsunami pueden llegar hasta 24 
horas después.</li></ul></div></div></div>|
<div class="slide" style="display: flex; height: 100vh; align-items: stretch; justify-content: center; overflow-x: auto; background-color: #fff;"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"><div class="column white" style="flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center; justify-content: center;"><div class="content" style="font-family: 'Arial', sans-serif;"><h1 style="color: #00a19a; font-family: 'Helvetica Neue', Arial, sans-serif;">Después de un tsunami</h1><ul style="list-style-type: disc; text-align: left;"><li style="font-size: 1.2em;">Permanece alejado de los escombros en el agua.</li><li style="font-size: 1.2em;">Vuelve a tu hogar cuando las autoridades comuniquen que la alerta ha sido levantada.</li><li style="font-size: 1.2em;">Al ingresar a tu vivienda, hazlo con precaución y abre las ventanas para secar el lugar. Retira el barro mientras esté húmedo.</li><li style="font-size: 1.2em;">Revisa el suministro de agua y alimentos, ya que pueden estar contaminados.</li><li style="font-size: 1.2em;">Junta agua potable por si se corta el suministro y hiérvela antes de beberla.</li><li style="font-size: 1.2em;">Mantente informado mediante una radio o televisión a pilas.</li><li style="font-size: 1.2em;">"""

    template = """Eres un orador de presentaciones de una mutual de seguridad.

    Vas a recibir diapositivas de una presentación organizada como html en donde cada diapositiva esta delimitada por el caracter barra vertical "|".
    Deberas narrar el contenido de texto dentro del html y las narraciones debe estar separadas por slices o diapositivas.
    
    El resultado será la narración de cada diapositiva en formato csv con delimitador el caracter barra vertical "|" al final de cada narración de diapositiva."""


    example_ai = """Serie Procedimientos Emergencias - Qué hacer en caso de tsunami|
Recomendaciones previas a un tsunami
- Infórmate si la comuna de tu lugar de trabajo tiene identificada la zona de inundación por tsunami.
- Revisa si el edificio en que trabajas se encuentra en una zona de fácil inundación.
- Identifica las vías de evacuación, puntos de encuentro y la zona sin riesgo de inundación por tsunami.|
Durante un tsunami
- Si estás en el borde costero y sientes un sismo violento, protégete con las tres reglas básicas: agáchate, cúbrete y afírmate.
- Evalúa si el terremoto rompió murallas o dificultó que te mantuvieras en pie. En estos casos, debes evacuar de forma inmediata y no intentar salvar tus pertenencias.
- Si recibes información oficial de alerta o alarma de tsunami, o ves que se recoge el mar, evacúa de inmediato a una zona libre de inundación a 30 metros de altura sobre el nivel del mar.
- Quédate en la zona segura hasta que las autoridades indiquen que es seguro regresar a tu hogar. Las olas de un tsunami pueden llegar hasta 24 horas después.|
Después de un tsunami
- Permanece alejado de los escombros en el agua.
- Vuelve a tu hogar cuando las autoridades comuniquen que la alerta ha sido levantada.
- Al ingresar a tu vivienda, hazlo con precaución y abre las ventanas para secar el lugar. Retira el barro mientras esté húmedo.
- Revisa el suministro de agua y alimentos, ya que pueden estar contaminados.
- Junta agua potable por si se corta el suministro y hiérvela antes de beberla.
- Mantente informado mediante una radio o televisión a pilas.
- Utiliza el teléfono solo para emergencias y preferiblemente mensajes de texto.|
Números de utilidad en caso de emergencia
Información que debe indicar
- Tipo de emergencia tsunami
- Número y estado general de lesionados
- Dirección y referencia de la emergencia
- ACHS SAMU|
Números de utilidad en caso de emergencia
Información que debe indicar
- Tipo de emergencia tsunami
- Dirección y cualquier otro dato que facilite su ubicación.|
¡Gracias por su atención!
Nombre del archivo: tsunami.pdf, Página: 1|
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
    print("NARRACCION ",result)
    return result

def playNarrator(text, engine):
    # Step 2: Generate the narrator voice
    engine.save_to_file(text, 'narration.wav')
    engine.runAndWait()

    # Step 3: Get the duration of the audio file
    audio = AudioSegment.from_wav('narration.wav')
    duration = round(audio.duration_seconds, 1)

    # Step 4: Use ffmpeg to play the audio !!!!!!!!!!!!!!!
    # Requiere tener ffmpeg instalado en el sistema y anadido al PATH como variable de entorno
    # with para que no se muestre el output de ffplay en la consola y generemos logs de mas (Se puede quitar para debug)
    with open(os.devnull, 'w') as devnull:
        subprocess.call(['ffplay', '-nodisp', '-autoexit', 'narration.wav'], stdout=devnull, stderr=devnull)

    # Step 5: Delete the file audio after playing
    os.remove('narration.wav')
    return duration


