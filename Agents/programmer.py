from langchain import PromptTemplate
from langchain.llms import OpenAI

import json


def askProgrammer(ask):
    with open("credentials.json", "r") as f:
        api = json.load(f)
        key = api["openai"]

    openai = OpenAI(
        model_name="gpt-3.5-turbo",
        openai_api_key=key,
        temperature=0.8,
    )

    template = """Create a html div with the proposed idea based on the context below to answer the question asked. If you cannot create it properly answer "I can't do it".

    Context: You are a professional web developer and you are working on a website for a client. Your job is to
    recieve the client's requirements and idea of the presentation and turn them into a presentation using html and css. You are expected to return
    a html div with the class "container" and a div with the class "content" inside of it, all of this for each slide of the presentation. There should be styles on most of the elements using css embeded
    inside of the html div. The client wants the website to have a background color of #0C652F and a font color of #FFFFFF. The output should be in json format, using a key value pair for each container div for a separate slide.

    Idea: {idea}

    Question: {question}
        """

    prompt_template = PromptTemplate(
        input_variables=["idea", "question"],
        template=template,
    )


    output = openai(
        prompt_template.format(
            idea="""Necesito una presentación que cumple con la separación de diapositivas, titulos,
            subtitulos, itemizadores y enumeradores que se demarcan en el texto""",
            question=ask,
        )
    )

    return(output)


response = askProgrammer("""
Diapositiva:
Titulo: Plan Nacional de Erradicación de la Silicosis (PLANESI)
Subtitulo: ¿Qué es el PLANESI?
item: Es el Plan Nacional de Erradicación de la Silicosis, promulgado por el Ministerio del Trabajo y Ministerio de Salud el 13 de Julio de 2007.
item: Sus objetivos estratégicos incluyen la disminución y control de la exposición a sílice en los lugares de trabajo, disminuir progresivamente la generación de silicosis y fortalecer la vigilancia ambiental y de la salud de los trabajadores expuestos.

Diapositiva:
Titulo: Normativa
Subtitulo: ¿Qué responsabilidad tiene la empresa asociada?
item: Informar a sus trabajadores de los riesgos de la sílice, medidas preventivas y métodos de trabajo.
item: Implementar un Sistema de Gestión de Seguridad y Salud en el Trabajo (SGSST) de acuerdo a las directrices de la OIT.
item: Implementar medidas necesarias de seguridad y de protección de la salud de los trabajadores.
item: Proporcionar a sus trabajadores elementos de protección personal.""")

print(response)
