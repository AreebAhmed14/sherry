from agents import Agent , Runner , function_tool , RunContextWrapper
from main import config
import os
import asyncio
from dataclasses import dataclass

@dataclass
class userInfo:
    age : int
    field : str
    sibling : str
    center_name : str
    goal : str

@function_tool
async def age_tool(wrapper : RunContextWrapper[userInfo]):
    return wrapper.context.age

@function_tool
async def field_tool(wrapper : RunContextWrapper[userInfo]):
    return wrapper.context.field

@function_tool
async def sibling_tool(wrapper : RunContextWrapper[userInfo]):
    return wrapper.context.sibling

@function_tool
async def center_name_tool(wrapper : RunContextWrapper[userInfo]):
    return wrapper.context.center_name
@function_tool
async def plan(wrapper : RunContextWrapper[userInfo]):
    return wrapper.context.goal

async def main():

    user_Info = userInfo(
        age = 18,
        field = "computer_science in 2025",
        sibling = "one brother and one sister",
        center_name = "Asian coaching center",
        goal = "To do own business"
    )

    agent = Agent[userInfo](
            name = "Sherry",
            instructions = os.getenv("sherry"),
            tools = [age_tool , field_tool , sibling_tool , center_name_tool , plan]
    )

    result = await Runner.run(
                agent,
                input = "tell shaheer school",
                run_config = config,
                context = user_Info
            ) 

    print(result.final_output)

asyncio.run(main())