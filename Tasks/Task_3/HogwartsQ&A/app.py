from fastapi import FastAPI
import numpy as np

app = FastAPI()

@app.post("/query")
async def query(query: str):
    # Generate the query embedding
    query_embedding = generate_embedding(query)  # Your function to generate embedding
    
    # Get top similar chunks
    top_chunks = get_top_k_similar(query_embedding, embeddings_np, chunks)
    
    return {"results": top_chunks}


from fastapi import FastAPI
from annoy import AnnoyIndex

app = FastAPI()

# Create and build the Annoy index
embedding_dim = len(embeddings[0])
annoy_index = AnnoyIndex(embedding_dim, 'angular')

for i, emb in enumerate(embeddings_np):
    annoy_index.add_item(i, emb)

annoy_index.build(10)

@app.post("/query")
async def query(query: str):
    # Generate the query embedding
    query_embedding = generate_embedding(query)
    
    # Get top similar chunks
    top_chunks = query_annoy(query_embedding)
    
    return {"results": top_chunks}


from fastapi import FastAPI
from sklearn.neighbors import NearestNeighbors

app = FastAPI()

# Fit the model
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings_np)

@app.post("/query")
async def query(query: str):
    # Generate the query embedding
    query_embedding = generate_embedding(query)
    
    # Get top similar chunks
    top_chunks = query_sklearn(query_embedding)
    
    return {"results": top_chunks}
