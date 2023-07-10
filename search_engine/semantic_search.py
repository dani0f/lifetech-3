from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from search_engine.read_files import load_files
from search_engine.load_embeddings import cargar_embeddings_desde_csv

def query(query):
    tokenizer = AutoTokenizer.from_pretrained("search_engine/model")
    model = AutoModel.from_pretrained("search_engine/model")
     
    documents = load_files("search_engine/dataset")
    document_embeddings = cargar_embeddings_desde_csv('search_engine/embeddings.csv')


    encoded_query = tokenizer.encode_plus(
        query,
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
    return documents[best_index]
    

#Detección en 0.45>
#HAcer la segmentación en el gpt
#print(query("incendio"))