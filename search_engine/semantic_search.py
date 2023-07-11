from nltk.corpus import stopwords
import nltk
import string
import torch
import re
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from transformers import AutoTokenizer, AutoModel
nltk.download('stopwords')

def preprocess_query(query):
    # Descargar recursos de NLTK si no están disponibles
    nltk.download('stopwords')

    # Tokenización
    tokens = query.lower().split()

    # Eliminación de palabras vacías
    stop_words = set(stopwords.words("spanish")) # Ajusta el idioma según corresponda
    tokens = [token for token in tokens if token not in stop_words]

    # Normalización
    tokens = [re.sub(r'[^\w\s]', '', token) for token in tokens]

    preprocessed_query = " ".join(tokens)
    return preprocessed_query

def query(query, documents, document_embeddings):
    preprocessed_query = preprocess_query(query)
    print("PROCESSQUERY:", preprocessed_query)
    tokenizer = AutoTokenizer.from_pretrained("search_engine/model")
    model = AutoModel.from_pretrained("search_engine/model")
     
    encoded_query = tokenizer.encode_plus(
        preprocessed_query,
        add_special_tokens=True,
        truncation=True,
        max_length=128,
        padding='max_length',
        return_tensors='pt'
    )

    with torch.no_grad():
        input_ids = encoded_query['input_ids']
        attention_mask = encoded_query['attention_mask']
        outputs = model(input_ids, attention_mask=attention_mask)
        query_embedding = torch.mean(outputs.last_hidden_state, dim=1).squeeze()
    
    similarity_scores = cosine_similarity(query_embedding.unsqueeze(0).numpy(), np.stack(document_embeddings))
    k = 1  
    best_index = np.argsort(similarity_scores, axis=1)[0][-k:][::-1][0]
    print(similarity_scores[0][best_index])
    if(similarity_scores[0][best_index] < 0.45):
        print("not found")
        return ""
    return documents[best_index]
