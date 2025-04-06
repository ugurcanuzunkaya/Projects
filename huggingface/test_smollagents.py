from smolagents import CodeAgent, LiteLLMModel
import litellm

model = LiteLLMModel(
    model_id="ollama/gemma3", # This model is a bit weak for agentic behaviours though
    api_base="http://localhost:11434", # replace with 127.0.0.1:11434 or remote open-ai compatible server if necessary
    # api_key="YOUR_API_KEY", # replace with API key if necessary
    num_ctx=8192, # ollama default is 2048 which will fail horribly. 8192 works for easy tasks, more is better. Check https://huggingface.co/spaces/NyxKrage/LLM-Model-VRAM-Calculator to calculate how much VRAM this will need for the selected model.
)

# litellm._turn_on_debug() # turn on debug mode to see the model's thought process

# Create a CodeAgent with the LiteLLMModel
agent = CodeAgent(tools=[], model=model, add_base_tools=True)

agent.run(
    "How is the weather in Eskişehir, Türkiye today?",
)