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


    example_human = """Nombre de archivo: qué-hacer-frente-a-un-robo-con-violencia-o-intimidación.pdf<Page:1>
ficha
técnica
gestión de riesgo de emergencia asalto
qué debo hacer frente a un asalto
todos nosotros, independiente del lugar donde nos encontremos, podemos sufrir un robo con violencia o intimidación. para prevenir estos
hechos y minimizar sus consecuencias, el trabajo en equipo es clave.
1. muy atento
observe su entorno al entrar, salir
y cuando esté ejecutando sus tareas
xxxxxxxxxxxxxxxxxxxxxxxx m sa in gi up iu el ne e ol ld ai sn e inr do cd ae m ioa nn ee r da d sis uc ere mta p,
xxxxxxxx
y d i c s e resa
resguarde sus objetos personales
manténgalos fuera de la vista de los
demás mientras cumple sus funciones
2. no te resistas
si estás siendo amenazado directamente si estás siendo retenido físicamente si estás alejado del núcleo del asalto
 baje su mirada a fin de evitar contacto visual  mantenga la calma a fin de proteger su  no huya del lugar si está en el campo
directo con el asaltante integridad y la de los demás visual del delincuente
 abra la caja y siga las instrucciones del  no oponga resistencia  retenga a las personas a su alcance que
asaltante intenten huir
 mantenga sus manos en alto y no oponga  no se acerque al lugar donde está
resistencia siendo realizado el asalto
3. ya pasó ahora, ayudémonos como equipo
si está llorando, no se angustie y siga estos pasos
separe a las personas más afectadas y manténgalas acompañadas
a. siéntese erguido y sin doblarse en sí mismo
b. mire hacia el frente
c. inspire suavemente y exhale
d. mantenga sus ojos abiertos mientras llora, lo ayudará a enfocarse en el presente
achs center 600 600 22 47  www.achs.cl"""
    
    template = """Eres un programador de html experto, recibiras la información de un instructivo y resumirla para hacer una presentación de diapositivas en html.
    
Para delimitar el inicio de una diapositiva deberás usar "<div class=”slide”>", para delimitar un titulo principal debes utilizar la etiqueta <h1>, para subtitulos la etiqueta <h2>, para las listas <ul>, para los enumeradores <ol>, para el texto <p>, para destacar <strong> y <i> para poner iconos de fontawesome que vayan deacuerdo al contexto de la diapositiva.
 
La salida esperada son los divisores de cada diapositiva de la presentación. El contenido de cada diapositiva debe tener como maximo 100 palabras y siempre debes empezar con una presentación de inicio y terminar la presentación con una diapositiva de "gracias por su atención".
"""

    example_ai ="""<div class="slide"><h1>FICHA TÉCNICA</h1><h2>Gestión de riesgo de emergencia asalto</h2><i class="fa-solid fa-people-robbery"></i></div>
<div class="slide"><h2>¿Qué debo hacer frente a un asalto?</h2><p>Todos nosotros, independiente del lugar donde nos encontremos, podemos sufrir un robo con violencia o intimidación. Para prevenir estos hechos y minimizar sus consecuencias, <strong>el trabajo en equipo es clave.</strong></p><i class="fa-solid fa-people-roof"></i></div>
<div class="slide"><h2>Consejos para enfrentar un asalto:</h2><ul><li>Manténgase muy atento y observe su entorno.</li><li>Resguarde sus objetos personales y manténgalos fuera de la vista de los demás.</li><li>No se resista si está siendo amenazado directamente.</li><li>Baje la mirada y mantenga la calma si está siendo retenido o alejado del núcleo del asalto.</li></ul><i class="fa-solid fa-triangle-exclamation"></i></div>
<div class="slide"><h2>Consejos adicionales durante el asalto:</h2><ul><li>Siga las instrucciones del asaltante y no oponga resistencia.</li><li>Mantenga sus manos en alto y no se acerque al lugar donde se está realizando el asalto.</li><li>Retenga a las personas a su alcance que intenten huir.</li></ul><i class="fa-solid fa-triangle-exclamation"></i></div>
<div class="slide"><h2>Después del asalto:</h2><ul><li>Separar a las personas más afectadas y mantenerlas acompañadas.</li><li>Siéntese erguido y mire hacia el frente.</li><li>Inspire suavemente y exhale para mantener la calma.</li><li>Mantenga los ojos abiertos mientras llora para enfocarse en el presente.</li></ul><i class="fa-solid fa-person-breastfeeding"></i></div>
<div class="slide"><h1>¡Gracias por su atención!</h1><p><strong>Nombre del archivo:</strong> qué-hacer-frente-a-un-robo-con-violencia-o-intimidación.pdf, página 1 ACHS CENTER: Teléfono 600 600 22 47, página web www.achs.cl</p><i class="fa-solid fa-circle-check"></i></div>"""

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
    result = chain.run(ask)
    print("summarizer", result)
    return result
 



