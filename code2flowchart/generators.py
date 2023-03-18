from langchain.llms import OpenAI

from code2flowchart.utils.flowchart.mermaid import generate_flowchart
from code2flowchart.templates.prompt import flowchart_template


def generate_output(code):
    llm = OpenAI(temperature=0.9)

    prompt = flowchart_template(
        f"""
        {code}
        """)
    res = llm(prompt)
    return generate_flowchart(res.replace('```', '').replace('mermaid', ''))


async def async_generate_output(file_name, code):
    llm = OpenAI(temperature=0.9)

    prompt = flowchart_template(
        f"""
        {code}
        """)
    res = await llm.agenerate([prompt])
    return generate_flowchart(file_name, res.generations[0][0].text.replace('```', ''))


