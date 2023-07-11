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

    example_human = """<div class="slide" style="display: flex; height: 100vh; align-items: stretch; justify-content: center; overflow-x: auto; font-family: 'Arial', sans-serif; background-color: #fff;"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"><div class="column white" style="flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center; justify-content: center;"><div class="content" style="text-align: center;"><h1 style="color: #00a19a;">FICHA TÉCNICA</h1><h2>Gestión de riesgo de emergencia asalto</h2><i class="fa-solid fa-exclamation-triangle" style="font-size: 5em; color: #00a19a;"></i><div style="display: flex; justify-content: center;"></div></div></div></div>|
<div class="slide" style="display: flex; height: 100vh; align-items: stretch; justify-content: center; overflow-x: auto; background-color: #fff;"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"><div class="column white" style="flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center; justify-content: center;"><div class="content" style="font-family: 'Arial', sans-serif;"><h1 style="color: #00a19a; font-family: 'Helvetica Neue', Arial, sans-serif;">¿Qué debo hacer frente a un asalto?</h1><p style="font-size: 1.2em; font-family: 'Arial', sans-serif;">Todos nosotros, independiente 
del lugar donde nos encontremos, podemos sufrir un robo con violencia o intimidación. Para prevenir estos hechos y minimizar sus consecuencias, el trabajo en equipo es clave.</p></div></div></div>|
<div class="slide" style="display: flex; height: 100vh; align-items: stretch; justify-content: center; overflow-x: auto; background-color: #fff; font-family: 'Arial', sans-serif;"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"><div class="column white" style="flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center;"><div class="content" style=""><h1  style="color: #00a19a;">Consejos para enfrentar un asalto</h1><ul style="list-style-type: disc; text-align: left;"><li style="font-size: 1.2em;">Manténgase muy atento y observe su entorno.</li><li style="font-size: 1.2em;">Resguarde sus objetos personales y manténgalos fuera de la vista de los demás.</li><li style="font-size: 1.2em;">No se resista si está siendo amenazado directamente.</li><li style="font-size: 1.2em;">Baje la mirada y mantenga la calma si está siendo retenido o alejado del núcleo del asalto.</li></ul></div></div></div>|
<div class="slide" style="display: flex; height: 100vh; align-items: stretch; justify-content: center; overflow-x: auto; background-color: #fff; font-family: 'Arial', sans-serif;"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"><div class="column white" style="flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center;"><div class="content" style=""><h1  style="color: #00a19a;">Consejos adicionales durante el asalto</h1><ul style="list-style-type: disc; text-align: left;"><li style="font-size: 1.2em;">Siga las instrucciones del asaltante y no oponga resistencia.</li><li style="font-size: 1.2em;">Mantenga sus manos en alto y no se acerque al lugar donde se está realizando el asalto.</li><li style="font-size: 1.2em;">Retenga a las personas a su alcance que intenten huir.</li></ul></div></div></div>|
<div class="slide" style="display: flex; height: 100vh; align-items: stretch; justify-content: center; overflow-x: auto; background-color: #fff; font-family: 'Arial', sans-serif;"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"><div class="column white" style="flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center;"><div class="content" style=""><h1  style="color: #00a19a;">Después del asalto</h1><p style="font-size: 1.2em;">Separar a las personas más afectadas y mantenerlas acompañadas.</p><ul style="list-style-type: disc; text-align: left;"><li style="font-size: 1.2em;">Siéntese erguido y mire hacia el frente.</li><li style="font-size: 1.2em;">Inspire suavemente y exhale para mantener la calma.</li><li style="font-size: 1.2em;">Mantenga los 
ojos abiertos mientras llora para enfocarse en el presente.</li></ul></div></div></div>|
<div class="slide" style="display: flex; height: 100vh; align-items: center; justify-content: center; background-color: #fff; font-family: 'Arial', sans-serif;"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"><div class="content" style="display: flex; flex-direction: column; align-items: center;"><h1 style="color: #00a19a; text-align: center;">¡Gracias por su atención!</h1><p style="font-size: 1.2em;">Nombre del archivo: qué-hacer-frente-a-un-robo-con-violencia-o-intimidación.pdf, página 1</p><p style="font-size: 1.2em;"><strong>ACHS CENTER:</strong> Teléfono 600 600 22 47, página web <a href="http://www.achs.cl">www.achs.cl</a></p></div></div>|"""

    template = """Eres un orador de presentaciones de una mutual de seguridad.

    Vas a recibir diapositivas de una presentación organizada como html en donde cada diapositiva esta delimitada por el caracter barra vertical "|".
    Deberas narrar el contenido de texto dentro del html y las narraciones debe estar separadas por slices o diapositivas.
    
    El resultado será la narración de cada diapositiva en formato csv con delimitador el caracter barra vertical "|" al final de cada narración de diapositiva."""


    example_ai = """FICHA TÉCNICA
Gestión de riesgo de emergencia asalto|

¿Qué debo hacer frente a un asalto?
Todos nosotros, independiente del lugar donde nos encontremos, podemos sufrir un robo con violencia o intimidación. Para prevenir estos hechos y minimizar sus consecuencias, el trabajo en equipo es clave.|

Consejos para enfrentar un asalto:

Manténgase muy atento y observe su entorno.
Resguarde sus objetos personales y manténgalos fuera de la vista de los demás.
No se resista si está siendo amenazado directamente.
Baje la mirada y mantenga la calma si está siendo retenido o alejado del núcleo del asalto.|

Consejos adicionales durante el asalto:

Siga las instrucciones del asaltante y no oponga resistencia.
Mantenga sus manos en alto y no se acerque al lugar donde se está realizando el asalto.
Retenga a las personas a su alcance que intenten huir.|

Después del asalto:

Separar a las personas más afectadas y mantenerlas acompañadas.
Siéntese erguido y mire hacia el frente.
Inspire suavemente y exhale para mantener la calma.
Mantenga los ojos abiertos mientras llora para enfocarse en el presente.|

¡Gracias por su atención!
Nombre del archivo: qué-hacer-frente-a-un-robo-con-violencia-o-intimidación.pdf, página 1
ACHS CENTER: Teléfono 600 600 22 47, página web www.achs.cl|
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


