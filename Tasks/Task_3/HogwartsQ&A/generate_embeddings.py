import json
import torch
from transformers import CLIPTokenizer, CLIPModel

# Load the CLIP model and tokenizer
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
tokenizer = CLIPTokenizer.from_pretrained("openai/clip-vit-base-patch32")

def generate_embeddings(text_chunks):
    embeddings = []
    for chunk in text_chunks:
        # Tokenize and get the embeddings
        inputs = tokenizer(chunk, return_tensors="pt", padding=True, truncation=True, max_length=77)
        with torch.no_grad():
            outputs = model.get_text_features(**inputs)
        # Convert the tensor to a list and add to embeddings list
        embeddings.append(outputs.cpu().numpy().flatten().tolist())
    return embeddings

# Load preprocessed chunks
with open("chunks.json", "r") as f:
    chunks = json.load(f)

# Generate embeddings for each chunk
embeddings = generate_embeddings(chunks)

# Save embeddings to a JSON file
with open("embeddings_clip.json", "w") as f:
    json.dump(embeddings, f)
