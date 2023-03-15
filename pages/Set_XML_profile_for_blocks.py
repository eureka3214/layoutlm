import streamlit as st
import fitz


tag_contents = {
    'objective': 'Learn about XML parsing',
    'chapter_name': 'Introduction to XML',
    'topic_name': 'What is XML?',
    'topic_contents': ['XML stands for eXtensible Markup Language...', 'XML is a markup language...'],
    'sub_topic_name': 'XML Syntax',
    'sub_topic_contents': ['XML syntax is fairly simple...', 'XML elements are defined...'],
    'None': 'nothing....'
}

def display_blocks(pdf_path):
    doc = fitz.open(stream=pdf_path.read(), filetype="pdf")
    pgno = st.number_input("Input page number", min_value=0)
    if pgno:
        page = doc[pgno]

        # read page text as a dictionary, suppressing extra spaces in CJK fonts
        blocks = page.get_text("dict")["blocks"]
        for i, b in enumerate(blocks): 
            with st.expander(f"Text Block {i}"):
                selected_value = st.selectbox(f"{i}", ['None','objective', 'chapter_name', 'topic_name', 'topic_contents','sub_topic_name','sub_topic_contents'])
                for l in b["lines"]:
                    for s in l["spans"]:
                        text = s["text"]
                        x = st.write(text)
                        # UPDATE tag_contents
                        if selected_value == 'topic_contents' or selected_value == 'sub_topic_contents':
                            if selected_value not in tag_contents:
                                tag_contents[selected_value] = []
                            tag_contents[selected_value].append(text)
                        else:
                            tag_contents[selected_value] = text

st.title("Set XML profile for selected blocks")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    display_blocks(uploaded_file)

st.write(tag_contents)
