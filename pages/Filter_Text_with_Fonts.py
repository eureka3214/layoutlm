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

def display_fonts(pdf_path, pagenum):
    doc = fitz.open(stream=pdf_path.read(), filetype="pdf")
    page = doc[pagenum]

    # read page text as a dictionary, suppressing extra spaces in CJK fonts
    blocks = page.get_text("dict", flags=11)["blocks"]
    font_properties_list = []
    for b in blocks:  # iterate through the text blocks
        for l in b["lines"]:  # iterate through the text lines
            for s in l["spans"]:  # iterate through the text spans
                font_properties = {
                    "font_name": s["font"],  # font name
                    "font_flags": flags_decomposer(s["flags"]),  # readable font flags
                    "font_size": s["size"],  # font size
                    "font_color": s["color"],  # font color
                    "text": s["text"],  # text
                }
                font_properties_list.append(font_properties)

    # Get unique font names, font sizes, and font colors
    font_names = list(set([fp["font_name"] for fp in font_properties_list]))
    font_sizes = list(set([fp["font_size"] for fp in font_properties_list]))
    font_colors = list(set([fp["font_color"] for fp in font_properties_list]))

    # Generate dropdowns for filtering
    selected_font_name = st.selectbox("Select font name", ["All"] + font_names)
    selected_font_size = st.selectbox("Select font size", ["All"] + [str(fs) for fs in font_sizes])
    selected_font_color = st.selectbox("Select font color", ["All"] + [str(fc) for fc in font_colors])

    # Show the filtered data
    for fp in font_properties_list:
        if (selected_font_name == "All" or fp["font_name"] == selected_font_name) and \
                (selected_font_size == "All" or fp["font_size"] == float(selected_font_size)) and \
                (selected_font_color == "All" or fp["font_color"] == int(selected_font_color, 16)):
            st.write("")
            font_properties = "Font: '%s' (%s), size %g, color #%06x" % (
                fp["font_name"],  # font name
                fp["font_flags"],  # readable font flags
                fp["font_size"],  # font size
                fp["font_color"],  # font color
            )
            st.write("Text: '%s'" % fp["text"])  # simple print of text
            st.code(font_properties)

st.title("Filter with Fonts (WORKING)")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    pgno = st.number_input("Input Page Number",min_value=0 )
    if pgno is not None:
        display_fonts(uploaded_file, pgno)