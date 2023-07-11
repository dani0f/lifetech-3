from search_engine.read_files import save_files
from search_engine.save_embeddings import save_embeddings_csv
import os

def generate_files():
    os.mkdir("search_engine\dataset")
    save_files("search_engine\documents","search_engine\dataset")
    save_embeddings_csv("search_engine\dataset","search_engine\embeddings.csv")