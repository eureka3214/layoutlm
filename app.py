import streamlit as st
import fitz
import layoutparser as lp
import numpy as np
import pandas as pd

def extract_layouts(pdf_path):
    doc = fitz.open(stream=pdf_path.read(), filetype="pdf")
    # page = doc[0]
    layouts = []
    for page in doc:
        txtpg = page.get_textpage()
        blocks = txtpg.extractBLOCKS()

        rect = page.rect
        width = rect.width
        height = rect.height
        # Get page dimensions
        # width, height = page.bound().size

        # Get page text and create blocks
        blocks = []
        for block in page.getText("dict")["blocks"]:
            bbox = block["bbox"]
            text = block["text"]
            st.write(bbox)
            st.write(text)

    #         blocks.append(lp.TextBlock(
    #             np.array([bbox[:2], bbox[2:], [bbox[0], bbox[3]], [bbox[2], bbox[1]]]),
    #             text))

    #     # Create a layout object for the page
    #     page_layout = lp.Layout(blocks, size=(width, height))

    #     # Add the page layout to the list
    #     layouts.append(page_layout)

    # return layouts

def main():
    st.title("PDF Layout Extractor")
    st.write("This app extracts the page layouts from a PDF file.")

    # Allow user to upload a PDF file
    pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    if pdf_file is not None:
        # Extract the page layouts
        layouts = extract_layouts(pdf_file)

        # Display the page layouts
        st.write(f"Number of pages: {len(layouts)}")
        for i, layout in enumerate(layouts):
            st.write(f"Page {i+1}")
            st.image(layout.to_image(), caption=f"Page {i+1} layout", use_column_width=True)

if __name__ == "__main__":
    main()
