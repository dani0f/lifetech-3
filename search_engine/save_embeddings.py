from transformers import AutoTokenizer, AutoModel
import torch
from read_files import load_files;


def embeddings(dir_input):
    tokenizer = AutoTokenizer.from_pretrained("search_engine/model")
    model = AutoModel.from_pretrained("search_engine/model")
    documents = load_files(dir_input)
    # Estos dos pasos siguientes se pueden pasar a otra función para hacer una base de datos de los embeddings de documentos
    # Preprocess and encode documents
    encoded_documents = []
    for doc in documents:
        encoded_input = tokenizer.encode_plus(
            doc,
            add_special_tokens=True,
            truncation=True,
            max_length=128,
            padding='max_length',
            return_tensors='pt'
        )
        encoded_documents.append(encoded_input)

    # Create document embeddings using BERT
    document_embeddings = []
    with torch.no_grad():
        for encoded_doc in encoded_documents:
            input_ids = encoded_doc['input_ids']
            attention_mask = encoded_doc['attention_mask']
            outputs = model(input_ids, attention_mask=attention_mask)
            doc_embedding = torch.mean(outputs.last_hidden_state, dim=1).squeeze()
            document_embeddings.append(doc_embedding)

    return document_embeddings



import csv

def guardar_embeddings_en_csv(embeddings, ruta_archivo):
    # Obtener la dimensión del embedding
    dimension_embedding = embeddings[0].shape[0]

    # Abrir el archivo CSV en modo escritura
    with open(ruta_archivo, 'w', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)

        # Escribir los encabezados de las columnas (dimensiones del embedding)
        encabezados = ['Dimensión {}'.format(i+1) for i in range(dimension_embedding)]
        writer.writerow(encabezados)

        # Escribir los embeddings
        for embedding in embeddings:
            writer.writerow(embedding.tolist())

    print("Los embeddings se han guardado en el archivo CSV correctamente.")

# Supongamos que tienes la lista de embeddings llamada 'document_embeddings' y la ruta del archivo CSV donde deseas guardarlos llamada 'ruta_archivo_csv'

dir_input = "search_engine\dataset"
document_embeddings = embeddings(dir_input)

ruta_archivo_csv = 'search_engine\embeddings.csv'
guardar_embeddings_en_csv(document_embeddings, ruta_archivo_csv)
