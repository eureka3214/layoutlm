import streamlit as st

# Define the dictionary that will be used to populate the XML tags
tag_contents = {
    'objective': 'Learn about XML parsing',
    'chapter_name': 'Introduction to XML',
    'topic_name': 'What is XML?',
    'topic_contents': 'XML stands for eXtensible Markup Language...',
    'sub_topic_name': 'XML Syntax',
    'sub_topic_contents': 'XML syntax is fairly simple...',
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
    return template.format(**dictionary)

# Define the Streamlit app
st.title("XML Generator")

# Display the dictionary values for reference
st.write("Dictionary contents:")
for key, value in tag_contents.items():
    st.write(f"{key}: {value}")

# Display the XML code generated from the template and dictionary
st.write("Generated XML code:")
xml_code = fill_template(xml_template, tag_contents)
st.code(xml_code, language="xml")
