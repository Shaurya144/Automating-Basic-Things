# Chapter 13 — PDFs and Word Documents

import PyPDF2
import docx

# read pdf
with open("example.pdf", "rb") as f:
    reader = PyPDF2.PdfReader(f)

    # number of pages
    print(len(reader.pages))

    # read first page text
    print(reader.pages[0].extract_text())

# create word document
doc = docx.Document()

# add paragraph
doc.add_paragraph("Hello world")

# save document
doc.save("example.docx")
