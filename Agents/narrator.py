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

    example_human = """<div class="slide"><h1>FICHA TÉCNICA</h1><h2>Gestión de riesgo de emergencia asalto</h2></div>
<div class="slide"><h2>¿Qué debo hacer frente a un asalto?</h2><p>Todos nosotros, independiente del lugar donde nos encontremos, podemos sufrir un robo con violencia o intimidación. Para prevenir estos hechos y minimizar sus consecuencias, <strong>el trabajo en equipo es clave.</strong></p></div>
<div class="slide"><h2>Consejos para enfrentar un asalto:</h2><ul><li>Manténgase muy atento y observe su entorno.</li><li>Resguarde sus objetos personales y manténgalos fuera de la vista de los demás.</li><li>No se resista si está siendo amenazado directamente.</li><li>Baje la mirada y mantenga la calma si está siendo retenido o alejado del núcleo del asalto.</li></ul></div>
<div class="slide"><h2>Consejos adicionales durante el asalto:</h2><ul><li>Siga las instrucciones del asaltante y no oponga resistencia.</li><li>Mantenga sus manos en alto y no se acerque al lugar donde se está realizando el asalto.</li><li>Retenga a las personas a su alcance que intenten huir.</li></ul></div>
<div class="slide"><h2>Después del asalto:</h2><ul><li>Separar a las personas más afectadas y mantenerlas acompañadas.</li><li>Siéntese erguido y mire hacia el frente.</li><li>Inspire suavemente y exhale para mantener la calma.</li><li>Mantenga los ojos abiertos mientras llora para enfocarse en el presente.</li></ul></div>
<div class="slide"><h1>¡Gracias por su atención!</h1><p><strong>Nombre del archivo:</strong> qué-hacer-frente-a-un-robo-con-violencia-o-intimidación.pdf, página 1 ACHS CENTER: Teléfono 600 600 22 47, página web www.achs.cl|</p></div>"""

    template = """Eres un orador de presentaciones de una mutual de seguridad.

    Vas a recibir diapositivas de una presentación organizada como html en donde cada diapositiva inicia con el divisor <div class="slide"> y termina con </div>.
    Deberas narrar el contenido de texto dentro del html y las narraciones debe estar separadas por slides o diapositivas.
    
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


