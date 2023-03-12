import streamlit as st
import layoutparser as lp

# Upload PDF file
pdf_file = st.file_uploader("Upload a PDF file", type="pdf")

# If a file was uploaded
if pdf_file is not None:
    # Read the contents of the file
    pdf_contents = pdf_file.read()
    layouts = lp.io.load_pdf(pdf_file)
    # Do something with the PDF contents
    st.write(layouts)
