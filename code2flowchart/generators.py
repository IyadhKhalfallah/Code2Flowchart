from langchain.llms import OpenAI

from utils.mermaid import generate_flowchart
from templates.prompt import flowchart_template

def generate_output(code):
    llm = OpenAI(temperature=0.9)

    prompt = flowchart_template(
        f"""
        {code}
        """)
    res = llm(prompt)
    return generate_flowchart(res.replace('```', ''))
