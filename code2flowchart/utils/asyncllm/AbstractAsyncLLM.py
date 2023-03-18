from abc import ABC, abstractmethod


class AbstractAsyncLLM(ABC):
    def __init__(self, temperature):
        self.temperature = temperature

    @abstractmethod
    async def async_generate(self):
        pass

    async def generate_concurrently(self):
        pass
