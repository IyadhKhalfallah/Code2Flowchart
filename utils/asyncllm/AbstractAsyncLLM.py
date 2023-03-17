import asyncio

from abc import ABC, abstractmethod
from langchain.llms import OpenAI


class AbstractAsyncLLM(ABC):
    def __init__(self, temperature):
        self.temperature = temperature

    @abstractmethod
    async def async_generate(self):
        pass

    async def generate_concurrently(self):
        llm = OpenAI(temperature=self.temperature)
        tasks = [self.async_generate(llm) for _ in range(10)]
        await asyncio.gather(*tasks)
