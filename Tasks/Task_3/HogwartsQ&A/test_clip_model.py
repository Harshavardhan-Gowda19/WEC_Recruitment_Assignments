import torch
from transformers import CLIPTokenizer, CLIPModel

# Load the model and tokenizer
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
tokenizer = CLIPTokenizer.from_pretrained("openai/clip-vit-base-patch32")

# Test encoding a simple query
test_query = "What is the significance of the Marauder’s Map?"
inputs = tokenizer(test_query, return_tensors="pt", padding=True, truncation=True, max_length=77)
with torch.no_grad():
    outputs = model.get_text_features(**inputs)

print(outputs)
