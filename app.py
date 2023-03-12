import streamlit as st
import io
import layoutparser as lp
import fitz
from PIL import Image


def visualize_layouts(pdf_file):
    # Convert PDF to images
    with io.BytesIO(pdf_file.read()) as pdf_buffer:
        doc = fitz.open(stream=pdf_buffer.read(), filetype="pdf")
        pil_images = []
        for page in doc:
            pix = page.get_pixmap(alpha=False)
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            pil_images.append(img)
    
    # Extract layouts
    # layouts = lp.models.Detectron2LayoutModel('lp://PubLayNet-faster_rcnn').detect(pil_images)
    
    # Display layouts
    

# Streamlit app
st.title('PDF Layout Visualizer')

pdf_file = st.file_uploader('Upload a PDF file', type='pdf')
if pdf_file is not None:

  pdf_layout = lp.load_pdf(pdf_file)
  # visualize_layouts(pdf_file)
  for page_layout in pdf_layout:
        page_image = pil_images[page_layout.page_number]
        st.image(page_image, use_column_width=True)
        for block in page_layout.blocks:
            st.write(f'Block {block.id} ({block.type}):')
            st.write(block)
            st.image(block.crop(page_image), use_column_width=True)

