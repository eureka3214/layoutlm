import streamlit as st
import fitz


def display_blocks(pdf_path):
    doc = fitz.open(stream=pdf_path.read(), filetype="pdf")
    pgno = st.number_input("Input page number", min_value=0)
    if pgno:
        page = doc[pgno]

        # read page text as a dictionary, suppressing extra spaces in CJK fonts
        blocks = page.get_text("dict")["blocks"]
        for i, b in enumerate(blocks):  # iterate through the text blocks
            with st.expander(f"Block {i}"):
                # iterate through the text lines in the block
                for l in b["lines"]:
                    # iterate through the text spans in the line
                    for s in l["spans"]:
                        text = s["text"]
                        # create a button for the line
                        # with st.expander(text):
                        block_xml = page.get_text("xml", b)
                            # with st.expander("Block XML"):
                        st.code(block_xml)


st.title("PDF get xml of selected block")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    display_blocks(uploaded_file)
