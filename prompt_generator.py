from langchain_core.prompts import PromptTemplate

# template
template = PromptTemplate(
    template="""
Please summarize the document of domain "{domain}" with the following specifications:
Explanation Style: {style_input}  
Explanation Length: {length_input}  
Document Content: {document_text}
Instructions:
- Include important concepts
- Explain equations simply if present
- Use analogies where helpful
- If information is missing, say so instead of guessing
""",
input_variables=['domain', 'style_input','length_input', 'document_text'],
validate_template=True
)

template.save('template.json')