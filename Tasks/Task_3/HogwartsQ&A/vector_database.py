import json
import numpy as np
import faiss

# Load embeddings and chunks
with open("embeddings_clip.json", "r") as f:
    embeddings = json.load(f)
with open("chunks.json", "r") as f:
    chunks = json.load(f)

# Convert embeddings to a numpy array
embedding_dim = len(embeddings[0])  # Get the dimension of embeddings
embeddings_np = np.array(embeddings).astype("float32")

# Initialize a FAISS index
index = faiss.IndexFlatL2(embedding_dim)  # L2 distance metric
index.add(embeddings_np)

def query_faiss(query_embedding, top_k=5):
    """Retrieve the top_k most similar chunks for a given query embedding."""
    query_embedding = np.array(query_embedding).astype("float32").reshape(1, -1)
    distances, indices = index.search(query_embedding, top_k)
    return [(chunks[idx], distances[i]) for i, idx in enumerate(indices[0])]

# Example usage:
# Let's say `query_embedding` is the embedding of the user's query (you'll need to generate it similarly to other chunks)
# query_embedding = ... # generate the embedding for a user query
# top_chunks = query_faiss(query_embedding)
# print(top_chunks)
