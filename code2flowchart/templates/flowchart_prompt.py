# "After you explained the code, generate a correct mermaid.js flowchart syntax to explain what every component of this code does."
from langchain import PromptTemplate


template = """
I want you to act as a flowchart expert.

Generate a correct mermaid.js flowchart syntax to explain the below code explanation:
CONTEXT_START
{code}
CONTEXT_END

the output of this should be only the mermaid.js flowchart syntax.
"""


def flowchart_template(code):
    prompt = PromptTemplate(
        input_variables=["code"],
        template=template,
    )

    return prompt.format(code=code)