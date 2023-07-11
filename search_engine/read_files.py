import os
import pdfplumber
import re

def preprocess(text):
    regex = r'[^a-zA-Z0-9áéíóúñÁÉÍÓÚÑ\s.,]'
    return re.sub(regex, '', text).lower()

def pdf_to_text(filename):
  with pdfplumber.open(filename) as temp:
    text = "Nombre de archivo: " + filename
    for p in temp.pages:
        text =  text + str(p) + "\n" + preprocess(p.extract_text())
  return text


def read_files_by_pages(dir):
    document_path = dir
    dir_list = os.listdir(document_path)
    documents = []
    for file in dir_list:
        if(file[-3:] == "pdf"):
            text = pdf_to_text(document_path + "/" + file)
            if(len(text) <= 7000):
                documents.append(text)
            while (len(text) > 7000) :
                documents.append(file + "\n" + text[:7000])
                text = text[7001:]

    return documents
    

def save_files(dir_input, dir_output):
    documents = read_files_by_pages(dir_input)
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


