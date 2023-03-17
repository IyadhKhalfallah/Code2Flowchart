from langchain import PromptTemplate


template = """
I want you to act as a senior code analyst.
Explain the code below in details:
{code}
After you explained the code, generate a correct mermaid.js flowchart syntax to explain what every component of this code does.
Output only the mermaid.js flowchart syntax.
"""


def flowchart_template(code):
    prompt = PromptTemplate(
        input_variables=["code"],
        template=template,
    )

    return prompt.format(code=code)