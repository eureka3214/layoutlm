import streamlit as st
import fitz


list ={}
def display_blocks(pdf_path):
    doc = fitz.open(stream=pdf_path.read(), filetype="pdf")
    pgno = st.number_input("Input page number", min_value=0)
    if pgno:
        page = doc[pgno]

        # read page text as a dictionary, suppressing extra spaces in CJK fonts
        blocks = page.get_text("dict")["blocks"]
        for i, b in enumerate(blocks): 
            with st.expander(f"Text Block {i}"):
                selected_value = st.selectbox(f"{i}", ['None','Objectives', 'sub_topic_name', 'sub_topic_Contents', 'Chapter'])
                for l in b["lines"]:
                    for s in l["spans"]:
                        text = s["text"]
                        st.write(text)
                        list[text] = selected_value

                        # st.write(text)
                        # selected_value = st.selectbox(f"{text}", ['Category 1', 'Category 2', 'Category 3', 'Category 4'])
                        # st.write("Appending content to", selected_value)
                        # st.session_state.(selected_value, []).append(text)

st.title("Set XML profile for selected blocks")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    display_blocks(uploaded_file)

st.write(list)