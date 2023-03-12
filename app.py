import streamlit as st
import layoutparser as lp
from pdf2image import convert_from_bytes

# Upload PDF file
pdf_file = st.file_uploader("Upload PDF", type=["pdf"])

if pdf_file is not None:
    # Convert PDF to PIL Image
    images = convert_from_bytes(pdf_file.read())
    st.success("PDF file uploaded successfully!")
    
    # Display images
    for i, image in enumerate(images):
        st.image(image, caption=f"Page {i+1}")
    
    # Extract layout from the first page
    layout = lp.Detectron2LayoutModel('lp://PubLayNet-frozen').detect(images[0])
    
    # Display bounding boxes
    with st.expander("Layout"):
        st.write(lp.draw_box(images[0], layout, box_width=2))
