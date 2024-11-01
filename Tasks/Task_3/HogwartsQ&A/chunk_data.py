import json

def chunk_text(text, chunk_size=150, overlap=30):
    # Split text into words
    words = text.split()
    chunks = []
    
    # Create chunks with overlap
    for i in range(0, len(words), chunk_size - overlap):
        chunk = words[i:i + chunk_size]
        # Join the words back into a string for each chunk
        chunks.append(" ".join(chunk))
    
    return chunks

# Load book text
with open("book_text.txt", "r") as f:
    book_text = f.read()

# Chunk the text
chunks = chunk_text(book_text)

# Save the chunks to a JSON file
with open("chunks.json", "w") as f:
    json.dump(chunks, f)
