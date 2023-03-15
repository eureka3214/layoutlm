import streamlit as st
import fitz


def display_blocks(pdf_path):
    doc = fitz.open(stream=pdf_path.read(), filetype="pdf")
    # page = doc[0]

    # read page text as a dictionary, suppressing extra spaces in CJK fonts
    for page in docs:
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:  # iterate through the text blocks
            for l in b["lines"]:  # iterate through the text lines
                for s in l["spans"]:
                    st.write(s["text"])
        
    # create radio buttons for each block
    block_index = st.radio("Select a block:", [i for i in range(len(blocks))])
    
    # get the XML content of the selected block
    if block_index:
        block_xml = page.get_text("xml", blocks[block_index])
        with st.expander("block XML"):
            st.code(block_xml)


st.title("PDF get xml")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    display_blocks(uploaded_file)
