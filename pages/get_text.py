import streamlit as st
import fitz


def display_blocks(pdf_path):
    doc = fitz.open(stream=pdf_path.read(), filetype="pdf")
    pgno = st.number_input("Input page number", min_value=0)
    if pgno:
        page = doc[pgno].get_textpage(3)

    # read page text as a dictionary, suppressing extra spaces in CJK fonts
        blocks = page.extractText()
        st.write(blocks)
      

st.title("PDF get text ")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    display_blocks(uploaded_file)