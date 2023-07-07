import os
import pdfplumber
import docx2txt
import re


def pdf_to_text(filename):
  text = ""
  with pdfplumber.open(filename) as temp:
    for p in temp.pages:
      text = text + p.extract_text()
  return text

def doc_to_text(filename):
    my_text = docx2txt.process(filename)
    return my_text

def read_files(dir):
    document_path = dir
    dir_list = os.listdir(document_path)
    documents = []
    for file in dir_list:
        print("read: ", document_path + "/" + file)
        if(file[-3:] == "pdf"):
            documents.append("Nombre archivo: " + file + "\n" + pdf_to_text(document_path + "/" + file))
        elif(file[-3] == "ocx"):
            documents.append("Nombre archivo: " + file + "\n" + doc_to_text(document_path + "/" + file))      
    return documents

def dividir_por_oraciones(texto):
    oraciones = re.split(r'(?<=[.!?])\s+', texto)
    return oraciones

def guardar_fragmentos(fragmentos, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        for fragmento in fragmentos:
            archivo.write(fragmento + '\n')

def save_fragments(dir):
    document_path = dir
    dir_list = os.listdir(document_path)
    fragmentos = []
    for file in dir_list:
        print("read: ", document_path + "/" + file)
        if(file[-3:] == "pdf"):
            texto = pdf_to_text(document_path + "/" + file)
            fragmentos.extend(dividir_por_oraciones(texto))
        elif(file[-3:] == "docx"):
            texto = doc_to_text(document_path + "/" + file)
            fragmentos.extend(dividir_por_oraciones(texto))

    guardar_fragmentos(fragmentos, "search_engine/fragments/fragmentos.txt")
    return fragmentos

#300 cada uno
print(save_fragments("search_engine/documents"))

def read_files(dir):
    document_path = dir
    dir_list = os.listdir(document_path)
    fragmentos = []
    for file in dir_list:
        print("read: ", document_path + "/" + file)
        if(file[-3:] == "pdf"):
            texto = pdf_to_text(document_path + "/" + file)
            fragmentos.extend(dividir_por_oraciones(texto))
        elif(file[-3:] == "docx"):
            texto = doc_to_text(document_path + "/" + file)
            fragmentos.extend(dividir_por_oraciones(texto))

    guardar_fragmentos(fragmentos, "fragmentos.txt")
    return fragmentos


def save_files(dir_input, dir_output):
    from read_files import read_files
    documents = read_files(dir_input)
    file = dir_output
    for i in range(len(documents)):
        with open(file + f'/doc_{i}.txt', 'w', encoding='utf-8') as f:
            f.write(documents[i])


def load_files(dir):
    document_path = dir
    dir_list = os.listdir(document_path)
    documents = []
    for file in dir_list:
        print("read: ", document_path + "/" + file)
        doc = ""
        with open(document_path + '/' + file, encoding='utf-8') as f:
            lines = f.readlines()
            doc = doc + "".join(lines)
        documents.append(doc)
    return documents

#print(load_files("dataset")[0])
