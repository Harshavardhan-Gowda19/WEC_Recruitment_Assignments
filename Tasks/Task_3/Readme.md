---

# Hogwarts Q&A: Harry Potter and the Prisoner of Azkaban

## Description

This project implements a Retrieval-Augmented Generation (RAG) system to answer questions from "Harry Potter and the Prisoner of Azkaban." Using natural language processing and machine learning, it retrieves and generates responses based on the book's context, covering characters, events, spells, and more.

## Features

- **RAG-based Q&A** for dynamic, contextually accurate responses
- **User-friendly Web Interface** for interactive queries
- **Enhanced Retrieval** using embeddings for contextually relevant sections

## Project Structure

```
HogwartsQ&A/
│
├── venv/                        # Virtual environment for dependencies
├── __pycache__/                 # Cached Python files
├── app.py                       # FastAPI application file
├── book_text.txt                # Extracted book text in plain text format
├── chunk_data.py                # Script for data chunking
├── chunks.json                  # JSON file with text chunks for retrieval
├── data_extraction.py           # Script for extracting and processing book data
├── embeddings_clip.json         # JSON file storing generated embeddings
├── generate_embeddings.py       # Script to create embeddings from book text
├── harry_potter_prisoner_of_azkaban.pdf  # Source PDF for the Q&A system
├── query_interface.py           # Command-line interface for Q&A
├── test_clip_model.py           # Script to test CLIP model
└── vector_database.py           # Script for vector database management

```

## Prerequisites

- Python 3.8+
- FastAPI, Uvicorn
- FAISS or alternative vector similarity library
- PyTorch (for embedding model)
- PyPDF2 (for PDF parsing)

## Setup

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd HogwartsQ&A
   ```

2. **Activate the virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

## Running the Application

1. **Generate embeddings** from the PDF:

   ```bash
   python generate_embeddings.py
   ```

2. **Start the FastAPI server**:

   ```bash
   uvicorn app:app --reload
   ```

3. **Open the Web Interface** at `http://localhost:8000` and enter your query.

## Technical Details

- **Custom Text Chunking** breaks down the book into manageable sections.
- **Manual Embedding and FAISS-free retrieval** using vector similarity.
- **Dynamic Answer Generation** based on the query input and context retrieved.

## Acknowledgments

- J.K. Rowling for the magical world of Harry Potter
- Open-source contributors for their invaluable tools and libraries
