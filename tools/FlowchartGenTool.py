import os
from langchain.tools import BaseTool
from utils.mermaid import generate_flowchart
from langchain.llms import OpenAI
from templates.flowchart_prompt import flowchart_template


class FlowchartGenTool(BaseTool):
    name = "Generate flowchart"
    description = (
        "A flowchart generator, which generates a flowchart out of some text explaining a code process."
        "Input should be a valid a detailed text explaining a process."
        ""
    )
    llm = OpenAI(temperature=0.9)

    def _run(self, query: str) -> str:
        """Use the tool."""
        code = self.llm(flowchart_template(query))
        return generate_flowchart(code.replace('`', ''))

    async def _arun(self, query: str) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("BingSearchRun does not support async")