import asyncio
from code2flowchart.utils.asyncllm.AbstractAsyncLLM import AbstractAsyncLLM


class AsyncLLM(AbstractAsyncLLM):
    def __init__(self, temperature):
        super().__init__(temperature)

    async def async_generate(self, llm):
        resp = await llm.agenerate(["Hello, how are you?"])
        print(resp.generations[0][0].text)


c = AsyncLLM(0)
loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(c.generate_concurrently()),
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
