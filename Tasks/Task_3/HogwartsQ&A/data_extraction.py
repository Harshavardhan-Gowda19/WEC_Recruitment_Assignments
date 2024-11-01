import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    with fitz.open(pdf_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text

pdf_path = "harry_potter_prisoner_of_azkaban.pdf"
book_text = extract_text_from_pdf(pdf_path)

# Save the extracted text
with open("book_text.txt", "w") as f:
    f.write(book_text)
