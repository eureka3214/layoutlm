import streamlit as st
import pdf2image

imagem_referencia = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png", "pdf", "tiff"])
button = st.button("Confirm")

if button and imagem_referencia is not None:

    if imagem_referencia.type == "application/pdf":
        images = pdf2image.convert_from_bytes(imagem_referencia.read())
        for page in images:
            st.image(page, use_column_width=True)