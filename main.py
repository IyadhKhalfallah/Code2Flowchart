import os
from langchain.llms import OpenAI
from utils.mermaid import generate_flowchart
from templates.prompt import flowchart_template
import streamlit as st


def generate_output(code):
    llm = OpenAI(temperature=0.9)

    prompt = flowchart_template(
        f"""
        {code}
        """)
    res = llm(prompt)
    return generate_flowchart(res.replace('```', ''))


def main():
    st.title("Flowchart generator from code")

    # Add a text input box for the Python code
    code = st.text_area("Enter your Python code here:")
    # Add a submit button
    if st.button("Run Code"):
        # Run the Python code and display the output
        output = generate_output(code)
        st.image(output, caption="Generated Image", use_column_width=True)

main()