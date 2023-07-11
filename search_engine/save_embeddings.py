from transformers import AutoTokenizer, AutoModel
import torch
import csv
import numpy as np
from search_engine.read_files import load_files

def generate_embeddings(dir_input):
    tokenizer = AutoTokenizer.from_pretrained("search_engine/model")
    model = AutoModel.from_pretrained("search_engine/model")
    documents = load_files(dir_input)
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

    document_embeddings = []
    with torch.no_grad():
        for encoded_doc in encoded_documents:
            input_ids = encoded_doc['input_ids']
            attention_mask = encoded_doc['attention_mask']
            outputs = model(input_ids, attention_mask=attention_mask)
            doc_embedding = torch.mean(outputs.last_hidden_state, dim=1).squeeze()
            document_embeddings.append(doc_embedding)

    return document_embeddings




def save_embeddings_csv(dir_input, dir_output):
    embeddings = generate_embeddings(dir_input)
    dimension_embedding = embeddings[0].shape[0]

    with open(dir_output, 'w', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)

        encabezados = ['Dimensión {}'.format(i+1) for i in range(dimension_embedding)]
        writer.writerow(encabezados)

        for embedding in embeddings:
            writer.writerow(embedding.tolist())





def load_embeddings(dir):
    embeddings = []
    with open(dir, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  

        for row in reader:
            embedding = np.array(row, dtype=np.float32)
            embeddings.append(embedding)

    return embeddings




