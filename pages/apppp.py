# import streamlit as st
# import fitz
# import layoutparser as lp

# def extract_layouts(pdf_path):
#     doc = fitz.open(stream=pdf_path.read(), filetype="pdf")
#     layouts = []
#     for page in doc:
#         img = page.get_pixmap()
#         image_size = lp.Rectangle(0, 0, img.width, img.height)
#         layout = lp.Layout(image_size)

#         # Extract text blocks and add them to the layout
#         for block in page.get_text("dict"):
#             bbox = lp(block["bbox"])
#             layout.add_text(
#                 block["text"], bbox,
#                 block_type="text",
#                 confidence=None
#             )

#         # Extract image blocks and add them to the layout
#         for i, img_block in enumerate(page.get_images(output="dict")):
#             bbox = lp.Rectangle(img_block["bbox"])
#             layout.add_image(
#                 f"image_{i}", bbox,
#                 block_type="image",
#                 metadata={"uri": img_block["image"]},
#                 confidence=None
#             )

#         layouts.append(layout)

#     return layouts

# st.title("PDF Layout Extractor")
# st.write("This app extracts the page layouts from a PDF file and shows bounding boxes around detected elements.")

# # Allow user to upload a PDF file
# pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])
# if pdf_file is not None:
#     layouts = extract_layouts(pdf_file)
#     # Display the page layouts
#     st.write(f"Number of pages: {len(layouts)}")
#     for i, layout in enumerate(layouts):
#         st.write(f"Page {i+1}")
#         st.image(layout.visualize(), caption=f"Page {i+1} layout with bounding boxes", use_column_width=True)
