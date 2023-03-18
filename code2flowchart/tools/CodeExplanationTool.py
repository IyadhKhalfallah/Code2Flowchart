from langchain.tools import BaseTool
from langchain.llms import OpenAI


class CodeExplanationTool(BaseTool):
    name = "Explain code"
    description = (
        "A text generator from code, which acts like a code analyst to explain a code in details."
        "Input should be a valid code in any programming language, found between CONTEXT_START and CONTEXT_END."
        ""
    )
    llm = OpenAI(temperature=0.9)

    def _run(self, query: str) -> str:
        """Use the tool."""
        return self.llm(query)

    async def _arun(self, query: str) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("CodeExplanationTool does not support async")