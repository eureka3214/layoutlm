import streamlit as st
import fitz


tag_contents = {
    'objective': 'Upload PDF, set page, and select from text block',
    'chapter_name': ' select chapter_name from text block',
    'topic_name': ' select topic_name from text block',
    'topic_contents': [' select topic_contents from text block', '......'],
    'sub_topic_name': ' select sub_topic_name from text block',
    'sub_topic_contents': [' select sub_topic_contents from text block', '...'],
    'None': 'nothing....'
}



# Define the XML template string
xml_template = """<Course>
    <Objectives>
        <Objective>{objective}</Objective>
    </Objectives>
    <Chapter>
        <Chapter_name>{chapter_name}</Chapter_name>
        <Topics>
            <Topic>
                <Topic_name>{topic_name}</Topic_name>
                <Contents>{topic_contents}</Contents>
                <sub_Topics>
                    <sub_Topic>
                        <sub_Topic_name>{sub_topic_name}</sub_Topic_name>
                        <sub_Topic_Contents>{sub_topic_contents}</sub_Topic_Contents>
                    </sub_Topic>
                </sub_Topics>
            </Topic>
        </Topics>
    </Chapter>
</Course>"""


# Define a function that replaces the placeholders in the XML template with the corresponding values from the dictionary
def fill_template(template, dictionary):
    # Join the topic_contents and sub_topic_contents lists into strings separated by newlines
    dictionary['topic_contents'] = '\n'.join(dictionary['topic_contents'])
    dictionary['sub_topic_contents'] = '\n'.join(dictionary['sub_topic_contents'])
    return template.format(**dictionary)



def display_blocks(pdf_path):
    doc = fitz.open(stream=pdf_path.read(), filetype="pdf")
    pgno = st.number_input("Input page number", min_value=0)
    if pgno:
        page = doc[pgno]

        # read page text as a dictionary, suppressing extra spaces in CJK fonts
        blocks = page.get_text("dict")["blocks"]
        for i, b in enumerate(blocks): 
            with st.expander(f"Text Block {i}"):
                selected_value = st.selectbox(f"{i}", ['None','objective', 'chapter_name', 'topic_name', 'topic_contents','sub_topic_name','sub_topic_contents'])
                for l in b["lines"]:
                    for s in l["spans"]:
                        text = s["text"]
                        x = st.write(text)
                        # UPDATE tag_contents
                        if selected_value == 'topic_contents' or selected_value == 'sub_topic_contents':
                            if selected_value not in tag_contents:
                                tag_contents[selected_value] = []
                            tag_contents[selected_value].append(text)
                        else:
                            tag_contents[selected_value] = text

st.title("Set XML profile for selected blocks")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    display_blocks(uploaded_file)

# st.write("Dictionary contents:")
# for key, value in tag_contents.items():
#     st.write(f"{key}: {value}")

# Display the XML code generated from the template and dictionary
st.subheader("Generated XML code:")
xml_code = fill_template(xml_template, tag_contents)
st.code(xml_code, language="xml")
