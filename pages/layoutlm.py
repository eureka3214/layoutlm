import streamlit as st
import layoutparser as lp
import fitz




# Select the first page of the PDF
# pdf_page = pdf_doc[0]

# # Convert the PDF page to a PNG image
# png_bytes = pdf_page.getPixmap().png

# # Write the PNG image to a file
# with open("output.png", "wb") as f:
#     f.write(png_bytes)


# Upload PDF file
pdf_file = st.file_uploader("Upload a PDF file", type="pdf")

# If a file was uploaded
if pdf_file is not None:
    pdf_doc = fitz.open(pdf_file)
    pdf_page = pdf_doc[0]
    # Read the contents of the file
    # pdf_contents = pdf_file.read()
    layouts = lp.io.load_pdf(pdf_file)
    # Do something with the PDF contents
    st.write(layouts)
