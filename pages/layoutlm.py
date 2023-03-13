import streamlit as st
import fitz
import layoutparser as lp

# Upload PDF file
pdf_file = st.file_uploader("Upload a PDF file", type="pdf")

if pdf_file is not None:
    # pdf_layout = lp.load_pdf(pdf_file)
    doc =  fitz.open(stream=pdf_file.read(), filetype="pdf")
    zoom = 4
    mat = fitz.Matrix(zoom, zoom)
    count = 0
    layout_doc = lp.load_pdf(pdf_file)
    for block in layout_doc:
        txtblock = lp.TextBlock
        for txtblock in block:
            coor = txtblock.coordinates
            st.write(coor)
        # if isinstance(block, lp.TextBlock):
        #     # Draw a red bounding box around the text block
        #     box = block.coordinates
        #     st.write(box)
        #     # img = lp.draw_box(img, box, color="red", thickness=2)
    # Count variable is to get the number of pages in the pdf
    # for p in doc:
    #     count += 1
    # for i in range(count):
    #     val = f"image_{i+1}.png"
    #     page = doc.load_page(i)
    #     pix = page.get_pixmap(matrix=mat)
    #     pix.save(val)
    #     st.image(val)

    doc.close()

