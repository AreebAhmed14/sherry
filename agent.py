from agents import Agent , Runner
from main import config
import os
import asyncio

def sherry(userq):
    agent = Agent(
        name = "Sherry",
        instructions = os.getenv("sherry"),
    )

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(
            Runner.run(
                agent,
                input = str(userq),
                run_config = config
            ) 
        )

    return(result.final_output)