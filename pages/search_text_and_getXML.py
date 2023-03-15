import streamlit as st
import fitz


def display_block_with_text(pdf_path, search_text):
    doc = fitz.open(stream=pdf_path.read(), filetype="pdf")
    page = doc[0]

    # read page text as a dictionary, suppressing extra spaces in CJK fonts
    blocks = page.get_text("dict")

    # search for the block containing the search text
    for block in blocks["blocks"]:
        if search_text in block["text"]:
            # get the XML content of the block containing the search text
            block_xml = page.get_text("xml", block=block)
            st.write(block_xml)
            break
    else:
        st.write(f"Paragraph with text '{search_text}' not found.")


st.title("PDF get xml")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    search_text = st.text_input("Enter the search text for the paragraph:")
    if search_text:
        display_block_with_text(uploaded_file, search_text)
