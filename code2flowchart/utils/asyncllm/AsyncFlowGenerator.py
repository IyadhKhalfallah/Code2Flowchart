import asyncio
import os
from code2flowchart.utils.asyncllm.AbstractAsyncLLM import AbstractAsyncLLM
from code2flowchart.utils.extractors.githubextractor import get_github_files
from code2flowchart.generators import async_generate_output

os.environ['OPENAI_API_KEY'] = 'OPENAI_KEY'


class AsyncFlowGenerator(AbstractAsyncLLM):
    def __init__(self, temperature):
        super().__init__(temperature)

    async def async_generate(self, file_name, code):
        await async_generate_output(file_name, code)

    async def generate_concurrently(self, owner, repo):
        git_files = get_github_files(owner, repo)
        tasks = [self.async_generate(file_name, code) for file_name, code in git_files.items()]
        await asyncio.gather(*tasks)
