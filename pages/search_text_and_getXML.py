import streamlit as st
import fitz


def display_blocks(pdf_path):
    doc = fitz.open(stream=pdf_path.read(), filetype="pdf")
    page = doc[0]

    # read page text as a dictionary, suppressing extra spaces in CJK fonts
    blocks = page.get_text("dict")["blocks"]
    
    # create radio buttons for each block
    block_index = st.radio("Select a block:", [i for i in range(len(blocks))])
    
    # get the XML content of the selected block
    block_xml = page.get_text("xml", blocks[block_index])
    st.write(block_xml)


st.title("PDF get xml")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    display_blocks(uploaded_file)