import asyncio
from dotenv import load_dotenv
load_dotenv()
from browser_use import Agent
from langchain_openai import ChatOpenAI
from browser import BrowserUseActivator
import time



# async def main():
#     activator = BrowserUseActivator()
# activator.activate()

#     agent = Agent(
#         task="Compare the price of gpt-4o and DeepSeek-V3",
#         llm=ChatOpenAI(model="gpt-4o"),
#     )
#     await agent.run()

async def worker_service():
    activator = BrowserUseActivator()

    agent = Agent(
        task="Go to https://shipmate-redwood-portal.lovable.app/ and sign in as operator01 / pass123, go to shipment service and reschdule all",
        llm=ChatOpenAI(model="gpt-4o")
    )
    while True:

        if activator.is_active():
            print("Service is active, performing work...")
            # Do your work here
            await agent.run()    
            time.sleep(5)
        else:
            print("Service inactive, waiting...")
            time.sleep(2)

asyncio.run(worker_service())
# asyncio.run(main())
