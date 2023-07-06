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
    print("asking")
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

    Contexto: Eres un diseñador gráfico profesional y estás trabajando en una página web para un cliente. Tu trabajo consiste utilizar las palabras que demarcan titulos (title), subtitulos (subtitle)
    texto (text), itemizador (item) y enumarador (enum) para crear una presentación de diapositivas (slides) utilizando html y css. Se espera que devuelvas
    un div html para cada diapositiva de la presentación. 
    La salida deberan ser los slides resultantes de la estilización delimitados por el caracter barra vertical |"""

    example_ai = """<div class="slide" style="display: flex; height: 100vh; align-items: stretch; justify-content: center; background-color: #00a19a; overflow-x: auto;"><div class="column white" style="flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center; justify-content: center;"><div class="content"><h1>FICHA TÉCNICA</h1><h2 style="color: #00a19a;">PROTOCOLO DE VIGILANCIA TRASTORNOS MUSCULOESQUELÉTICOS RELACIONADOS AL TRABAJO (TMERT)</h2></div></div></div>|
    <div class="slide" style="display: flex; height: 100vh; align-items: stretch; justify-content: center; background-color: #00a19a; overflow-x: auto;"><div class="column white" style="flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center; justify-content: center;"><div class="content"><h1>¿Qué es el Protocolo TMERT?</h1><h2 style="color: #00a19a;">Procedimiento y objetivos</h2><p>Es un procedimiento que entrega directrices para la prevención y control de los trastornos musculoesqueléticos (TME) de las extremidades superiores en las empresas. Contempla la identificación y evaluaciones de factores de riesgo biomecánicos, organizacionales y psicosociales en los puestos de trabajo, además de la vigilancia a la salud de los trabajadores expuestos.</p></div></div></div>|
    <div class="slide" style="display: flex; height: 100vh; align-items: stretch; justify-content: center; background-color: #00a19a; overflow-x: auto;"><div class="column white" style="flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center; justify-content: center;"><div class="content"><h1>Normativa asociada</h1><h2 style="color: #00a19a;">Responsabilidades de la empresa</h2></div></div><div class="column" style="flex: 1; padding: 2rem; color: #fff;"><div class="content"><ul style="list-style-type: disc;"><li>Evaluar los factores de riesgos detectados y aplicar un programa de control del riesgo.</li><li>Eliminar o mitigar los riesgos detectados y aplicar un programa de control del riesgo.</li><li>Informar a los trabajadores sobre los factores a los que están expuestos, las medidas preventivas y los métodos de trabajo correctos.</li><li>Cumplir con la Norma Técnica MINSAL TMERT de extremidades superiores y el Protocolo de Vigilancia para trabajadores expuestos a factores de riesgo de TMERT.</li></ul></div></div></div>|
    <div class="slide" style="display: flex; height: 100vh; align-items: stretch; justify-content: center; background-color: #00a19a; overflow-x: auto;"><div class="column" style="flex: 1; padding: 2rem; color: #fff;"><div class="content"><h1>Fiscalización de las Mutualidades de Empleadores</h1></div></div><div class="column white" style="flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center; justify-content: center;"><div class="content"><ol><li>Superintendencia de Seguridad Social: <a href="http://www.suseso.cl">www.suseso.cl</a></li><li>ACHS CENTER: Teléfono 600 600 22 47, página web <a href="http://www.achs.cl">www.achs.cl</a></li></ol></div></div></div>|
    <div class="slide" style="display: flex; height: 100vh; align-items: stretch; justify-content: center; background-color: #00a19a; overflow-x: auto;"><div class="column white" style="flex: 1; padding: 2rem; color: #000; background-color: #fff; display: flex; align-items: center; justify-content: center;"><div class="content"><h1>¡Gracias por su atención!</h1><h2 style="color: #00a19a;">Fuentes:</h2><div class="paragraphs" style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;"><div></div><div><p>Nombre del archivo: protocolos-ministerio-de-salud-trastornos-musculoesqueléticos-relacionados-al-trabajo-tmert.pdf</p></div></div></div></div></div>|"""


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


    result=chain.run(ask)
    print(result)
    return result.split("|")





