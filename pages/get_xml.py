import streamlit as st
import fitz

def flags_decomposer(flags):
    """Make font flags human readable."""
    l = []
    if flags & 2 ** 0:
        l.append("superscript")
    if flags & 2 ** 1:
        l.append("italic")
    if flags & 2 ** 2:
        l.append("serifed")
    else:
        l.append("sans")
    if flags & 2 ** 3:
        l.append("monospaced")
    else:
        l.append("proportional")
    if flags & 2 ** 4:
        l.append("bold")
    return ", ".join(l)

def display_fonts(pdf_path):
    doc = fitz.open(stream=pdf_path.read(), filetype="pdf")
    page = doc[0]

    # read page text as a dictionary, suppressing extra spaces in CJK fonts
    blocks = page.get_text("xml")
    st.write(blocks)
    # for b in blocks:  # iterate through the text blocks
    #     # lines = b["lines"]
    #     st.write(b)
    #     # for l in b["lines"]:  # iterate through the text lines
        #     for s in l["spans"]:  # iterate through the text spans
        #         st.write("")
        #         font_properties = "Font: '%s' (%s), size %g, color #%06x" % (
        #             s["font"],  # font name
        #             flags_decomposer(s["flags"]),  # readable font flags
        #             s["size"],  # font size
        #             s["color"],  # font color
        #         )
        #         st.write("Text: '%s'" % s["text"])  # simple print of text
        #         st.write(font_properties)

st.title("PDF get xml ")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    display_fonts(uploaded_file)