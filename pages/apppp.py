import streamlit as st
import fitz
import layoutparser as lp

# Upload PDF file
pdf_file = st.file_uploader("Upload a PDF file", type="pdf")
# model = lp.Detectron2LayoutModel('lp://HJDataset/faster_rcnn_R_50_FPN_3x/config')
st.write(model)
# If a file was uploaded
if pdf_file is not None:
    # pdf_layout = lp.load_pdf(pdf_file)
    doc =  fitz.open(stream=pdf_file.read(), filetype="pdf")
    zoom = 4
    mat = fitz.Matrix(zoom, zoom)
    count = 0
    
    # Count variable is to get the number of pages in the pdf
    for p in doc:
        count += 1
    for i in range(count):
        val = f"image_{i+1}.png"
        page = doc.load_page(i)
        pix = page.get_pixmap(matrix=mat)
        pix.save(val)
        # pdf_layout = model.detect(val)
        # annot= lp.visualization.draw_box(val,pdf_layout)
        # st.write(annot)
        st.image(val)

        # pdf_layout = lp.load_pdf(val)
        
    doc.close()

