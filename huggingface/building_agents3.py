from smolagents import ToolCallingAgent, DuckDuckGoSearchTool, HfApiModel
from huggingface_hub import login
from dotenv import load_dotenv
import os
load_dotenv()

login(token=os.getenv("SMOLAGENTS_TOKEN"))

agent = ToolCallingAgent(tools=[DuckDuckGoSearchTool()], model=HfApiModel())

agent.run("Search for the best music recommendations for a party at the Wayne's mansion.")