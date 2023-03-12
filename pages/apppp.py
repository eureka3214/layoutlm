import streamlit as st
import fitz
import layoutparser as lp

# Upload PDF file
pdf_file = st.file_uploader("Upload a PDF file", type="pdf")

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
        st.write(page)
        pix = page.get_pixmap(matrix=mat)
        pix.save(val)
        st.image(val)

        # pdf_layout = lp.load_pdf(val)
        
    doc.close()


    pdf_layout = lp.load_pdf(pdf_file)
    annot= lp.visualization.draw_box(val,pdf_layout)
    st.write(annot)
    
    # st.write(pdf_layout)

    # model = lp.Detectron2LayoutModel('lp://PubLayNet_Faster_R-CNN')
#     layout = model.detect(pil_image)

#     # Draw the bounding boxes on the PDF page
#     annotated_pdf = lp.draw_box(pdf_file, layout, page_id=0)

#     # Export the annotated PDF as an HTML file
#     html_io = BytesIO()
#     annotated_pdf.save(html_io, "html")
#     html_str = html_io.getvalue().decode()

#     # Display the HTML file in the Streamlit app
#     st.components.v1.html(html_str, width=700, height=800)
