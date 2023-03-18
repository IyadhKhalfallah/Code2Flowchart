import asyncio
from code2flowchart.utils.asyncllm.AsyncFlowGenerator import AsyncFlowGenerator


def run():
    async_llm = AsyncFlowGenerator(0)
    loop = asyncio.get_event_loop()
    tasks = [
        loop.create_task(async_llm.generate_concurrently('IyadhKhalfallah', 'aws-lambda_terraform')),
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == '__main__':
    run()
