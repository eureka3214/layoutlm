import streamlit as st
import fitz


def display_fonts(pdf_path):
    doc = fitz.open(stream=pdf_path.read(), filetype="pdf")
    page = doc[0]

    # read page text as a dictionary, suppressing extra spaces in CJK fonts
    blocks = page.get_text("xml")
    st.write(blocks)
  

st.title("PDF get xml ")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    display_fonts(uploaded_file)