from transformers import AutoTokenizer, AutoModel

def download_model():
    tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/multi-qa-mpnet-base-dot-v1")
    model = AutoModel.from_pretrained("sentence-transformers/multi-qa-mpnet-base-dot-v1")
    tokenizer.save_pretrained("search_engine\model")
    model.save_pretrained("search_engine\model")