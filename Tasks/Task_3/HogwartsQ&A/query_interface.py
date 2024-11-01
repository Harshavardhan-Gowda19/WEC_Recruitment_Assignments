import json
import numpy as np
import torch
from transformers import CLIPTokenizer, CLIPModel
import faiss

# Load the FAISS index, embeddings, and chunks
with open("embeddings_clip.json", "r") as f:
    embeddings = json.load(f)
with open("chunks.json", "r") as f:
    chunks = json.load(f)

embedding_dim = len(embeddings[0])
embeddings_np = np.array(embeddings).astype("float32")
index = faiss.IndexFlatL2(embedding_dim)
index.add(embeddings_np)

# Load the CLIP model and tokenizer
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
tokenizer = CLIPTokenizer.from_pretrained("openai/clip-vit-base-patch32")

def generate_query_embedding(query_text):
    inputs = tokenizer(query_text, return_tensors="pt", padding=True, truncation=True, max_length=77)
    with torch.no_grad():
        query_embedding = model.get_text_features(**inputs).cpu().numpy().flatten().tolist()
    return query_embedding

def query_faiss(query_embedding, top_k=5):
    """Retrieve the top_k most similar chunks for a given query embedding."""
    query_embedding = np.array(query_embedding).astype("float32").reshape(1, -1)
    distances, indices = index.search(query_embedding, top_k)
    
    # Ensure we handle cases where fewer than top_k results are found
    results = []
    for i, idx in enumerate(indices[0]):
        if idx < len(chunks):  # Ensure index is within bounds
            results.append((chunks[idx], distances[i]))
    return results


if __name__ == "__main__":
    while True:
        user_query = input("Enter your question (or 'exit' to quit): ")
        if user_query.lower() == 'exit':
            break
        
        try:
            query_embedding = generate_query_embedding(user_query)
            top_chunks = query_faiss(query_embedding, top_k=5)

            print("Top relevant chunks:")
            for chunk, distance in top_chunks:
                print(f"Chunk: {chunk} \nDistance: {distance}\n")

        except Exception as e:
            print(f"An error occurred: {e}")
