import streamlit as st
import fitz

def display_blocks(pdf_path):
    doc = fitz.open(stream=pdf_path.read(), filetype="pdf")
    pgno = st.number_input("Input page number", min_value=0)
    if pgno:
        page = doc[pgno]

        # read page text as a dictionary, suppressing extra spaces in CJK fonts
        blocks = page.get_text("dict")["blocks"]
        for i, b in enumerate(blocks): 
            with st.expander(f"Text Block {i}"):
                # iterate through the text lines in the block
                for l in b["lines"]:
                    # iterate through the text spans in the line
                    for s in l["spans"]:
                        text = s["text"]
                        st.write(text)
                        selected_value = st.selectbox(f"Select a category for Text Block {i}", ['Category 1', 'Category 2', 'Category 3', 'Category 4'])
                        st.write("Appending content to", selected_value)
                        st.session_state.setdefault(selected_value, []).append(b["text"])

st.title("Set XML profile for selected blocks")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    display_blocks(uploaded_file)

# Display the content for each category
st.write("Content for each category:")
for category, content_list in st.session_state.items():
    if category not in ['_legacy_config', '_is_running']:
        st.write(f"Category {category}:")
        for content in content_list:
            st.write(content)
