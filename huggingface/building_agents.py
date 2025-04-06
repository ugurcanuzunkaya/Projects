from huggingface_hub import login
from dotenv import load_dotenv
import os
load_dotenv()
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel, tool
import numpy as np
import datetime
import time



login(token=os.getenv("SMOLAGENTS_TOKEN"))

agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=HfApiModel())

agent.run(
    "Search for the best music recommendations for a party at the Wayne's mansion."
)


# Tool to suggest a menu based on the occasion
@tool
def suggest_menu(occasion: str) -> str:
    """
    Suggests a menu based on the occasion.
    Args:
        occasion (str): The type of occasion for the party. Allowed values are:
                        - "casual": Menu for casual party.
                        - "formal": Menu for formal party.
                        - "superhero": Menu for superhero party.
                        - "custom": Custom menu.
    """
    if occasion == "casual":
        return "Pizza, snacks, and drinks."
    elif occasion == "formal":
        return "3-course dinner with wine and dessert."
    elif occasion == "superhero":
        return "Buffet with high-energy and healthy food."
    else:
        return "Custom menu for the butler."

# Alfred, the butler, preparing the menu for the party
agent = CodeAgent(tools=[suggest_menu], model=HfApiModel())

# Preparing the menu for the party
agent.run("Prepare a formal menu for the party.")


agent = CodeAgent(tools=[], model=HfApiModel(), additional_authorized_imports=['datetime'])

agent.run(
    """
    Alfred needs to prepare for the party. Here are the tasks:
    1. Prepare the drinks - 30 minutes
    2. Decorate the mansion - 60 minutes
    3. Set up the menu - 45 minutes
    4. Prepare the music and playlist - 45 minutes

    If we start right now, at what time will the party be ready?
    """
)


# Change to your username and repo name
agent.push_to_hub('mrrelaxed/AlfredAgentTest')

# Change to your username and repo name
alfred_agent = agent.from_hub('mrrelaxed/AlfredAgentTest', trust_remote_code=True)

alfred_agent.run("Give me the best playlist for a party at Wayne's mansion. The party idea is a 'villain masquerade' theme")  

