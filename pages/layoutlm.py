import streamlit as st
import layoutparser as lp
import fitz
from io import BytesIO
from PIL import Image



# Upload PDF file
pdf_file = st.file_uploader("Upload a PDF file", type="pdf")

# If a file was uploaded
if pdf_file is not None:
    pdf_doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    pdf_page = pdf_doc[0]
    # png_bytes = pdf_page.get_pixmap()


# if "pixmaps" in pdf_page.get_displaylist():nnn
    # Convert the PDF page to a PIL Image object
    pixmap = pdf_page.get_pixmap()
    pil_image = Image.frombytes(
        mode="RGB",
        size=(pixmap.height,pixmap.width),
        data=pixmap.samples
    )

    # Convert the PIL Image object to bytes
    bytes_io = BytesIO()
    pil = pil_image.save(bytes_io, format="PNG")
    pixmap = bytes_io.getvalue()
    st.image(pixmap, caption="PDF Page 1 as PNG")


    # with open("output.png", "wb") as f:
    #     f.write(png_bytes)
    # Read the contents of the file
    # pdf_contents = pdf_file.read()
    layouts = lp.io.load_pdf(pdf_file)
    lp.draw_box(pixmap, pdf_layout[0])

    # Do something with the PDF contents
    # st.write(layouts)
