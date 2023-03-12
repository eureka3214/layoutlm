import fitz
from io import BytesIO
import layoutparser as lp
import streamlit as st


# Upload PDF file
pdf_file = st.file_uploader("Upload a PDF file", type="pdf")

# If a file was uploaded
if pdf_file is not None:
    # Open the PDF file
    # pdf_file = "example.pdf"
    pdf_doc = fitz.open(stream=pdf_file.read(), filetype="pdf")

    # Get the first page of the PDF as an image
    pdf_page = pdf_doc[0]
    pixmap = pdf_page.get_pixmap()
    png_bytes = pixmap.getImageData(output="png")

    # Convert the PNG image to a PIL Image object
    png_io = BytesIO(png_bytes)
    pil_image = Image.open(png_io)

    # Run the layout analysis on the PIL Image object
    model = lp.Detectron2LayoutModel('lp://PubLayNet_Faster_R-CNN')
    layout = model.detect(pil_image)

    # Draw the bounding boxes on the PDF page
    annotated_pdf = lp.draw_box(pdf_file, layout, page_id=0)

    # Export the annotated PDF as an HTML file
    html_io = BytesIO()
    annotated_pdf.save(html_io, "html")
    html_str = html_io.getvalue().decode()

    # Display the HTML file in the Streamlit app
    st.components.v1.html(html_str, width=700, height=800)
