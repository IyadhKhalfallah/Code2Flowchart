import os
from langchain.tools import BaseTool
from utils.mermaid import generate_flowchart
from langchain.llms import OpenAI


class FlowchartGenTool(BaseTool):
    name = "Generate flowchart"
    description = (
        "A flowchart generates, which acts like a code analyst to explain a code then generate a flowchart out of it"
        "Input should be a valid python code, found between CONTEXT_START and CONTEXT_END. "
        ""
    )
    llm = OpenAI(temperature=0.9)

    def _run(self, query: str) -> str:
        """Use the tool."""
        return generate_flowchart(query)

    async def _arun(self, query: str) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("BingSearchRun does not support async")