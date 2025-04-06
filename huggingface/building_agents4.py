from smolagents import CodeAgent, HfApiModel, tool, Tool, load_tool
from huggingface_hub import login
from dotenv import load_dotenv
import os
load_dotenv()

# Login to Hugging Face Hub. Make sure to set the SMOLAGENTS_TOKEN in your environment variables.
SMOLAGENTS_TOKEN = os.getenv("SMOLAGENTS_TOKEN")
login(token=SMOLAGENTS_TOKEN)
type_of_work = "push_tool" # push_tool, load_tool, hf_space_import
type_of_tool = "@tool" # @tool, class tool


if type_of_tool == "@tool":
    # Let's pretend we have a function that fetches the highest-rated catering services.
    @tool
    def catering_service_tool(query: str) -> str:
        """
        This tool returns the highest-rated catering service in Gotham City.

        Args:
            query: A search term for finding catering services.
        """
        # Example list of catering services and their ratings
        services = {
            "Gotham Catering Co.": 4.9,
            "Wayne Manor Catering": 4.8,
            "Gotham City Events": 4.7,
        }

        # Find the highest rated catering service (simulating search query filtering)
        best_service = max(services, key=services.get)

        return best_service


    agent = CodeAgent(tools=[catering_service_tool], model=HfApiModel())

    # Run the agent to find the best catering service
    result = agent.run(
        "Can you give me the name of the highest-rated catering service in Gotham City?"
    )

    print(result)   # Output: Gotham Catering Co.

elif type_of_tool == "class tool":
    class SuperheroPartyThemeTool(Tool):
        name = "superhero_party_theme_generator"
        description = """
        This tool suggests creative superhero-themed party ideas based on a category.
        It returns a unique party theme idea."""

        inputs = {
            "category": {
                "type": "string",
                "description": "The type of superhero party (e.g., 'classic heroes', 'villain masquerade', 'futuristic Gotham').",
            }
        }

        output_type = "string"

        def forward(self, category: str):
            themes = {
                "classic heroes": "Justice League Gala: Guests come dressed as their favorite DC heroes with themed cocktails like 'The Kryptonite Punch'.",
                "villain masquerade": "Gotham Rogues' Ball: A mysterious masquerade where guests dress as classic Batman villains.",
                "futuristic Gotham": "Neo-Gotham Night: A cyberpunk-style party inspired by Batman Beyond, with neon decorations and futuristic gadgets."
            }

            return themes.get(category.lower(), "Themed party idea not found. Try 'classic heroes', 'villain masquerade', or 'futuristic Gotham'.")

    # Instantiate the tool
    party_theme_tool = SuperheroPartyThemeTool()
    agent = CodeAgent(tools=[party_theme_tool], model=HfApiModel())

    # Run the agent to generate a party theme idea
    result = agent.run(
        "What would be a good superhero party idea for a 'villain masquerade' theme?"
    )

    print(result)  # Output: "Gotham Rogues' Ball: A mysterious masquerade where guests dress as classic Batman villains."

if type_of_work in ["class tool", "push_tool"]:
    # Push the tool to Hugging Face Hub
    party_theme_tool.push_to_hub("mrrelaxed/party_theme_tool", token=SMOLAGENTS_TOKEN)


elif type_of_work == "load_tool":
    # Load a pre-defined tool from Hugging Face Hub
    image_generation_tool = load_tool(
        "m-ric/text-to-image",
        trust_remote_code=True
    )

    agent = CodeAgent(
        tools=[image_generation_tool],
        model=HfApiModel()
    )

    agent.run("Generate an image of a luxurious superhero-themed party at Wayne Manor with made-up superheros.")


elif type_of_work == "hf_space_import":
    image_generation_tool = Tool.from_space(
        "black-forest-labs/FLUX.1-schnell",
        name="image_generator",
        description="Generate an image from a prompt"
    )

    model = HfApiModel("Qwen/Qwen2.5-Coder-32B-Instruct")

    agent = CodeAgent(tools=[image_generation_tool], model=model)

    agent.run(
        "Improve this prompt, then generate an image of it.",
        additional_args={'user_prompt': 'A grand superhero-themed party at Wayne Manor, with Alfred overseeing a luxurious gala'}
    )

elif type_of_work == "langchain_import":
    from langchain.agents import load_tools
    
    model = HfApiModel("Qwen/Qwen2.5-Coder-32B-Instruct")

    search_tool = Tool.from_langchain(load_tools(["serpapi"])[0])

    agent = CodeAgent(tools=[search_tool], model=model)

    agent.run("Search for luxury entertainment ideas for a superhero-themed event, such as live performances and interactive experiences.")

elif type_of_work == "mcp_import":
    from smolagents import ToolCollection
    from mcp import StdioServerParameters

    model = HfApiModel("Qwen/Qwen2.5-Coder-32B-Instruct")

    server_parameters = StdioServerParameters(
        command="uvx",
        args=["--quiet", "pubmedmcp@0.1.3"],
        env={"UV_PYTHON": "3.12", **os.environ},
    )

    with ToolCollection.from_mcp(server_parameters, trust_remote_code=True) as tool_collection:
        agent = CodeAgent(tools=[*tool_collection.tools], model=model, add_base_tools=True)
        agent.run("Please find a remedy for hangover.")

