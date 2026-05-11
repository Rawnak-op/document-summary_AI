from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from pypdf import PdfReader
from langchain_core.prompts import PromptTemplate, load_prompt
from typer import style

load_dotenv()
model = ChatGroq(
    model="llama-3.3-70b-versatile"
)

st.header("Document Summary")

domain=st.selectbox("Select domain of document",["Computer Science","Electronics","Electrical","Mechanical","Civil","Metallurgy","Biotechnology","Chemical","Mathematics","Physics","Chemistry"])

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Research-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

template = load_prompt('template.json')

# Button
if st.button("Generate Summary"):

    if uploaded_file is None:
        st.warning("Please upload a PDF")
    else:

        # Read PDF
        reader = PdfReader(uploaded_file)

        document_text = ""

        for page in reader.pages:

            text = page.extract_text()

            if text:
                document_text += text

        # Optional safety limit
        document_text = document_text[:12000]

        # Format prompt
        chain=template|model 
        result = chain.invoke({

            "domain": domain,
            "style_input": style_input,
            "length_input": length_input,
            "document_text": document_text
        })

        # Generate response

        # Output
        st.subheader("Summary")

        st.write(result.content)

