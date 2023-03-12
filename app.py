import streamlit as st
import fitz
import layoutparser as lp
import numpy as np
import pandas as pd

def extract_layouts(pdf_path):
    doc = fitz.open(stream=pdf_path.read(), filetype="pdf")
    xref = doc.get_new_xref()
    IMge = doc.extract_image(xref)
    canvas = IMge
    
    # page = doc[0]
    layouts = []
    for page in doc:

        txtpg = page.get_textpage()
        blocks = txtpg.extractDICT()
        # st.write(blocks)
        blks=[]
        rect = page.rect
        width = rect.width
        height = rect.height
        for block in blocks:
            blks.append(block)

    #     # Create a layout object for the page
        page_layout = lp.Layout(blks)

    #     # Add the page layout to the list
        layouts.append(page_layout)

    return layouts

def main():
    st.title("PDF Layout Extractor")
    st.write("This app extracts the page layouts from a PDF file.")

    # Allow user to upload a PDF file
    pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    if pdf_file is not None:
        # Extract the page layouts
        
        # Display the page layouts
    st.write(f"Number of pages: {len(layouts)}")
    for i, layout in enumerate(layouts):
        st.write(f"Page {i+1}")
        st.write(layout)
        layouts = extract_layouts(pdf_file)
        lp.visualization.draw_text(canvas, layout)

        
            # st.image(layout.to_image(), caption=f"Page {i+1} layout", use_column_width=True)

if __name__ == "__main__":
    main()
