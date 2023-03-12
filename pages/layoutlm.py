import streamlit as st
import layoutparser as lp
import fitz


# Upload PDF file
pdf_file = st.file_uploader("Upload a PDF file", type="pdf")

# If a file was uploaded
if pdf_file is not None:
    pdf_doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    pdf_page = pdf_doc[0]
    png_bytes = pdf_page.get_pixmap()
    with open("output.png", "wb") as f:
        f.write(png_bytes)
    # Read the contents of the file
    # pdf_contents = pdf_file.read()
    layouts = lp.io.load_pdf(pdf_file)
    # Do something with the PDF contents
    # st.write(layouts)
