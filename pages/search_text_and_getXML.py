import streamlit as st
import fitz


def display_blocks(pdf_path):
    doc = fitz.open(stream=pdf_path.read(), filetype="pdf")
    page = doc[0]

    # read page text as a dictionary, suppressing extra spaces in CJK fonts
    blocks = page.get_text("dict")["blocks"]
    
    # create radio buttons for each block
    options = {}
    for i, block in enumerate(blocks):
        line = block["lines"][0]["spans"][0]["text"]
        options[f"{i}: {line}"] = i
    block_index = st.radio("Select a block:", list(options.keys()), format_func=lambda x: x.split(": ")[1], index=0, key="radio")
    
    # get the XML content of the selected block
    if block_index:
        block_xml = page.get_text("xml", blocks[block_index])
        with st.expander("block XML"):
            st.code(block_xml)


st.title("PDF get xml")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    display_blocks(uploaded_file)
