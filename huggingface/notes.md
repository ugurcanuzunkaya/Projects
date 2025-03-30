# Agents Course

## Unit 1: Introduction to Agents

- Where we are building a solid foundation for understanding agents and their environments.
  - Understanding Agents
    - What is an Agent, and how does it work?
    - How do Agents make decisions using reasoning and planning?

- The Role of LLMs (Large Language Models) in Agents
  - How LLMs serve as the “brain” behind an Agent.
  - How LLMs structure conversations via the Messages system.

- Tools and Actions
  - How Agents use external tools to interact with the environment.
  - How to build and integrate tools for your Agent.

- The Agent Workflow:
  - Think → Act → Observe.

### What is an Agent?

- Agent receives a command, understands the natural language, it engages in reasoning and planning, and then it act with the tools that it has and knows.

- Agent has two main parts: the brain (AI Model) and the body (Capabilities and Tools).
  - The brain (AI Model)
    - This is where all the thinking happens. The AI model handles reasoning and planning. It decides which Actions to take based on the situation.
  - The body (Capabilities and Tools)
    - This part represents everything the Agent is equipped to do.
    - The scope of possible actions depends on what the agent has been equipped with. For example, because humans lack wings, they can’t perform the “fly” Action, but they can execute Actions like “walk”, “run” ,“jump”, “grab”, and so on.

- Type of AI Models we use for Agents
  - LLM (Large Language Models): the common one which takes Text (natural language) as input and produces Text as output.
  - Other AI Models: like Vision Models, Speech Models, etc.

- Type of tasks can an Agent do
  - It can do any task we implement via Tools to complete the Actions.
  - The design of the Tools is very important and has a great impact on the quality of your Agent. Some tasks will require very specific Tools to be crafted, while others may be solved with general purpose tools like “web_search”.
  - Note: Actions are not the same as Tools. An Action, for instance, can involve the use of multiple Tools to complete.
  - Allowing an agent to interact with its environment allows real-life usage for companies and individuals.

- Examples:
  - Personal Virtual Assistant: Virtual assistants like Siri, Alexa, or Google Assistant, work as agents when they interact on behalf of users using their digital environments. They take user queries, analyze context, retrieve information from databases, and provide responses or initiate actions (like setting reminders, sending messages, or controlling smart devices).
  - Customer Service Agents: Many companies deploy chatbots as agents that interact with customers in natural language. These agents can answer questions, guide users through troubleshooting steps, open issues in internal databases, or even complete transactions. Their predefined objectives might include improving user satisfaction, reducing wait times, or increasing sales conversion rates. By interacting directly with customers, learning from the dialogues, and adapting their responses over time, they demonstrate the core principles of an agent in action.
  - AI Non-Playable Characters (NPCs): AI agents powered by LLMs can make Non-Playable Characters (NPCs) more dynamic and unpredictable. Instead of following rigid behavior trees, they can respond contextually, adapt to player interactions, and generate more nuanced dialogue. This flexibility helps create more lifelike, engaging characters that evolve alongside the player’s actions.

- To summarize, an Agent is a system that uses an AI Model (typically an LLM) as its core reasoning engine, to:
  - **Understand natural language**: Interpret and respond to human instructions in a meaningful way.
  - **Reason and plan**: Analyze information, make decisions, and devise strategies to solve problems.
  - **Interact with its environment**: Gather information, take actions, and observe the results of those actions.

### What are LLMs?

- An LLM (Large Language Model) is a type of AI model that excels at understanding and generating human language. They are trained on vast amounts of text data, allowing them to learn patterns, structure, and even nuance in language. These models typically consist of many millions of parameters.
- Most LLMs nowadays are built on the Transformer architecture—a deep learning architecture based on the “Attention” algorithm, that has gained significant interest since the release of BERT from Google in 2018. [Transformers Architecture Image](image.png)

- 3 type of Transformers:
  - **Encoders**: An encoder-based Transformer takes text (or other data) as input and outputs a dense representation (or embedding) of that text. Example: BERT from Google. Use Cases: Text classification, semantic search, Named Entity Recognition. Typical Size: Millions of parameters
  - **Decoders**: A decoder-based Transformer focuses on generating new tokens to complete a sequence, one token at a time. Example: Llama from Meta. Use Cases: Text generation, chatbots, code generation. Typical Size: Billions (in the US sense, i.e., 10^9) of parameters
  - **Seq2Seq (Encoder-Decoder)**: A sequence-to-sequence Transformer combines an encoder and a decoder. The encoder first processes the input sequence into a context representation, then the decoder generates an output sequence. Example: T5, BART. Use Cases: Translation, Summarization, Paraphrasing. Typical Size: Millions of parameters

- Although Large Language Models come in various forms, LLMs are typically decoder-based models with billions of parameters. Most known examples: Deepseek-R1 - DeepSeek, GPT4 - OpenAI, Llama 3 - Meta (Facebook AI Research), SmolLM2 - Hugging Face, Gemma - Google, Mistral - Mistral.

- The underlying principle of an LLM is simple yet highly effective: its objective is to predict the next token, given a sequence of previous tokens. A “token” is the unit of information an LLM works with. You can think of a “token” as if it was a “word”, but for efficiency reasons LLMs don’t use whole words. Tokenization often works on sub-word units that can be combined. For instance, consider how the tokens “interest” and “ing” can be combined to form “interesting”, or “ed” can be appended to form “interested.”

- Each LLM has some special tokens specific to the model. The LLM uses these tokens to open and close the structured components of its generation. For example, to indicate the start or end of a sequence, message, or response. Moreover, the input prompts that we pass to the model are also structured with special tokens. The most important of those is the End of sequence token (EOS). The forms of special tokens are highly diverse across model providers.

- The table below illustrates the diversity of special tokens.

<table>
  <thead>
    <tr>
      <th><strong>Model</strong></th>
      <th><strong>Provider</strong></th>
      <th><strong>EOS Token</strong></th>
      <th><strong>Functionality</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>GPT4</strong></td>
      <td>OpenAI</td>
      <td><code>&lt;|endoftext|&gt;</code></td>
      <td>End of message text</td>
    </tr>
    <tr>
      <td><strong>Llama 3</strong></td>
      <td>Meta (Facebook AI Research)</td>
      <td><code>&lt;|eot_id|&gt;</code></td>
      <td>End of sequence</td>
    </tr>
    <tr>
      <td><strong>Deepseek-R1</strong></td>
      <td>DeepSeek</td>
      <td><code>&lt;|end_of_sentence|&gt;</code></td>
      <td>End of message text</td>
    </tr>
    <tr>
      <td><strong>SmolLM2</strong></td>
      <td>Hugging Face</td>
      <td><code>&lt;|im_end|&gt;</code></td>
      <td>End of instruction or message</td>
    </tr>
    <tr>
      <td><strong>Gemma</strong></td>
      <td>Google</td>
      <td><code>&lt;end_of_turn&gt;</code></td>
      <td>End of conversation turn</td>
    </tr>
  </tbody>
</table>

#### Understanding Next Token Prediction

- LLMs are said to be autoregressive, meaning that the output from one pass becomes the input for the next one. This loop continues until the model predicts the next token to be the EOS token, at which point the model can stop. In other words, an LLM will decode text until it reaches the EOS. But what happens during a single decoding loop?

- While the full process can be quite technical for the purpose of learning agents, here’s a brief overview:
  - Once the input text is tokenized, the model computes a representation of the sequence that captures information about the meaning and the position of each token in the input sequence.
  - This representation goes into the model, which outputs scores that rank the likelihood of each token in its vocabulary as being the next one in the sequence.
- Based on these scores, we have multiple strategies to select the tokens to complete the sentence.
  - The easiest decoding strategy would be to always take the token with the maximum score.
- But there are more advanced decoding strategies. For example, beam search explores multiple candidate sequences to find the one with the maximum total score–even if some individual tokens have lower scores.

#### Attention is all you need

- A key aspect of the Transformer architecture is Attention. When predicting the next word, not every word in a sentence is equally important.
- This process of identifying the most relevant words to predict the next token has proven to be incredibly effective. Although the basic principle of LLMs—predicting the next token—has remained consistent since GPT-2, there have been significant advancements in scaling neural networks and making the attention mechanism work for longer and longer sequences.
- If you’ve interacted with LLMs, you’re probably familiar with the term context length, which refers to the maximum number of tokens the LLM can process, and the maximum attention span it has.

#### Prompting the LLM is important

- Considering that the only job of an LLM is to predict the next token by looking at every input token, and to choose which tokens are “important”, the wording of your input sequence is very important.
- The input sequence you provide an LLM is called a prompt. Careful design of the prompt makes it easier to guide the generation of the LLM toward the desired output.

#### How are LLMs trained?

- LLMs are trained on large datasets of text, where they learn to predict the next word in a sequence through a self-supervised or masked language modeling objective.
- From this unsupervised learning, the model learns the structure of the language and underlying patterns in text, allowing the model to generalize to unseen data.
- After this initial pre-training, LLMs can be fine-tuned on a supervised learning objective to perform specific tasks.

#### How can I use LLMs?

- You have two main options:
  - Run Locally: You can run LLMs on your local machine or server. This requires you to have the necessary hardware and software to run the model.
  - Use a Cloud Service: You can use a cloud service that provides access to LLMs. This is a more convenient option, as it doesn’t require you to set up the model on your own machine.

#### How are LLMs used in AI Agents?

- LLMs are a key component of AI Agents, providing the foundation for understanding and generating human language.
- They can interpret user instructions, maintain context in conversations, define a plan and decide which tools to use.

### Messages and Special Tokens

- Let’s look at how they structure their generations through chat templates.
- When you chat with systems like ChatGPT or HuggingChat, you’re actually exchanging messages. Behind the scenes, these messages are concatenated and formatted into a prompt that the model can understand. [Frontend vs Backend Version of the Chat](image-1.png)
- They act as the bridge between conversational messages (user and assistant turns) and the specific formatting requirements of your chosen LLM.

#### Messages: The Underlying System of LLMs

- System Messages
  - System messages (also called System Prompts) define how the model should behave. They serve as persistent instructions, guiding every subsequent interaction.
  - When using Agents, the System Message also gives information about the available tools, provides instructions to the model on how to format the actions to take, and includes guidelines on how the thought process should be segmented.

#### Conversations: User and Assistant Messages

- Chat templates help maintain context by preserving conversation history, storing previous exchanges between the user and the assistant. This leads to more coherent multi-turn conversations.
- We always concatenate all the messages in the conversation and pass it to the LLM as a single stand-alone sequence. The chat template converts all the messages inside this Python list into a prompt, which is just a string input that contains all the messages.
- Templates can handle complex multi-turn conversations while maintaining context.

#### Chat-Templates

- Chat templates are essential for structuring conversations between language models and users. They guide how message exchanges are formatted into a single prompt.

##### Base Models vs. Instruct Models

- A Base Model is trained on raw text data to predict the next token.
- An Instruct Model is fine-tuned specifically to follow instructions and engage in conversations. For example, SmolLM2-135M is a base model, while SmolLM2-135M-Instruct is its instruction-tuned variant.
- To make a Base Model behave like an instruct model, we need to format our prompts in a consistent way that the model can understand. This is where chat templates come in.
- ChatML is one such template format that structures conversations with clear role indicators (system, user, assistant). If you have interacted with some AI API lately, you know that’s the standard practice.
- It’s important to note that a base model could be fine-tuned on different chat templates, so when we’re using an instruct model we need to make sure we’re using the correct chat template.

##### Understanding Chat Templates

- Because each instruct model uses different conversation formats and special tokens, chat templates are implemented to ensure that we correctly format the prompt the way each model expects.
- In transformers, chat templates include Jinja2 code that describes how to transform the ChatML list of JSON messages into a textual representation of the system-level instructions, user messages and assistant responses that the model can understand.
- This structure helps maintain consistency across interactions and ensures the model responds appropriately to different types of inputs.
- The transformers library will take care of chat templates for you as part of the tokenization process. All we have to do is structure our messages in the correct way and the tokenizer will take care of the rest.

##### Messages to Prompt

- The easiest way to ensure your LLM receives a conversation correctly formatted is to use the chat_template from the model’s tokenizer.
- To convert the previous conversation into a prompt, we load the tokenizer and call apply_chat_template
- The rendered_prompt returned by this function is now ready to use as the input for the model you chose!
- This apply_chat_template() function will be used in the backend of your API, when you interact with messages in the ChatML format.

### What are Tools?

- One crucial aspect of AI Agents is their ability to take actions. As we saw, this happens through the use of Tools.

#### What are AI Tools?

- A Tool is a function given to the LLM. This function should fulfill a clear objective.
- Here are some commonly used tools in AI agents:

| Tool | Description |
| --- | --- |
| Web Search | Allows the agent to fetch up-to-date information from the internet. |
| Image Generation | Creates images based on text descriptions. |
| Retrieval | Retrieves information from an external source. |
| API Interface | Interacts with an external API (GitHub, YouTube, Spotify, etc.). |

- Those are only examples, as you can in fact create a tool for any use case!
- A good tool should be something that complements the power of an LLM.
- For instance, if you need to perform arithmetic, giving a calculator tool to your LLM will provide better results than relying on the native capabilities of the model.
- Furthermore, LLMs predict the completion of a prompt based on their training data, which means that their internal knowledge only includes events prior to their training. Therefore, if your agent needs up-to-date data you must provide it through some tool.
- For instance, if you ask an LLM directly (without a search tool) for today’s weather, the LLM will potentially hallucinate random weather.

- A Tool should contain:
  - A textual description of what the function does.
  - A Callable (something to perform an action).
  - Arguments with typings.
  - (Optional) Outputs with typings.

#### How do tools work?

- LLMs can only receive text inputs and generate text outputs. They have no way to call tools on their own. What we mean when we talk about providing tools to an Agent, is that we teach the LLM about the existence of tools, and ask the model to generate text that will invoke tools when it needs to.
- The LLM will generate text, in the form of code, to invoke that tool. It is the responsibility of the Agent to parse the LLM’s output, recognize that a tool call is required, and invoke the tool on the LLM’s behalf. The output from the tool will then be sent back to the LLM, which will compose its final response for the user.
- The output from a tool call is another type of message in the conversation. Tool calling steps are typically not shown to the user: the Agent retrieves the conversation, calls the tool(s), gets the outputs, adds them as a new conversation message, and sends the updated conversation to the LLM again. From the user’s point of view, it’s like the LLM had used the tool, but in fact it was our application code (the Agent) who did it.

#### How do we give tools to an LLM?

- We essentially use the system prompt to provide textual descriptions of available tools to the model.
- For this to work, we have to be very precise and accurate about:
  - What the tool does
  - What exact inputs it expects

- This is the reason why tool descriptions are usually provided using expressive but precise structures, such as computer languages or JSON. It’s not necessary to do it like that, any precise and coherent format would work.

- Let’s understand it through a concrete example.
  - We will implement a simplified calculator tool that will just multiply two integers. This could be our Python implementation:
  
    ```python
      def calculator(a: int, b: int) -> int:
        """Multiply two integers."""
        return a * b
    ```

  - So our tool is called calculator, it multiplies two integers, and it requires the following inputs:
    - a (int): An integer.
    - b (int): An integer.

  - The output of the tool is another integer number that we can describe like this:
    - (int): The product of a and b.

  - All of these details are important. Let’s put them together in a text string that describes our tool for the LLM to understand.

    ```json
      Tool Name: calculator, Description: Multiply two integers., Arguments: a: int, b: int, Outputs: int
    ```

  - Reminder: This textual description is what we want the LLM to know about the tool.

- When we pass the previous string as part of the input to the LLM, the model will recognize it as a tool, and will know what it needs to pass as inputs and what to expect from the output.
- If we want to provide additional tools, we must be consistent and always use the same format. This process can be fragile, and we might accidentally overlook some details.

#### Auto-formatting Tools Sections

- Our tool was written in Python, and the implementation already provides everything we need:
  - A descriptive name of what it does: calculator
  - A longer description, provided by the function’s docstring comment: Multiply two integers.
  - The inputs and their type: the function clearly expects two ints.
  - The type of the output.

- There’s a reason people use programming languages: they are expressive, concise, and precise.
- We could provide the Python source code as the specification of the tool for the LLM, but the way the tool is implemented does not matter. All that matters is its name, what it does, the inputs it expects and the output it provides.
- We will leverage Python’s introspection features to leverage the source code and build a tool description automatically for us. All we need is that the tool implementation uses type hints, docstrings, and sensible function names. We will write some code to extract the relevant portions from the source code.
- After we are done, we’ll only need to use a Python decorator to indicate that the calculator function is a tool:

  ```python
  @tool
  def calculator(a: int, b: int) -> int:
      """Multiply two integers."""
      return a * b

  print(calculator.to_string())
  ```

- Note the @tool decorator before the function definition.
- With the implementation we’ll see next, we will be able to retrieve the following text automatically from the source code via the to_string() function provided by the decorator:

  ```json
  Tool Name: calculator, Description: Multiply two integers., Arguments: a: int, b: int, Outputs: int
  ```

- As you can see, it’s the same thing we wrote manually before!

#### Generic Tool Implementation

- We create a generic Tool class that we can reuse whenever we need to use a tool. Disclaimer: This example implementation is fictional but closely resembles real implementations in most libraries.

```python
class Tool:
    """
    A class representing a reusable piece of code (Tool).

    Attributes:
        name (str): Name of the tool.
        description (str): A textual description of what the tool does.
        func (callable): The function this tool wraps.
        arguments (list): A list of argument.
        outputs (str or list): The return type(s) of the wrapped function.
    """
    def __init__(self,
                 name: str,
                 description: str,
                 func: callable,
                 arguments: list,
                 outputs: str):
        self.name = name
        self.description = description
        self.func = func
        self.arguments = arguments
        self.outputs = outputs

    def to_string(self) -> str:
        """
        Return a string representation of the tool,
        including its name, description, arguments, and outputs.
        """
        args_str = ", ".join([
            f"{arg_name}: {arg_type}" for arg_name, arg_type in self.arguments
        ])

        return (
            f"Tool Name: {self.name},"
            f" Description: {self.description},"
            f" Arguments: {args_str},"
            f" Outputs: {self.outputs}"
        )

    def __call__(self, *args, **kwargs):
        """
        Invoke the underlying function (callable) with provided arguments.
        """
        return self.func(*args, **kwargs)
```

- It may seem complicated, but if we go slowly through it we can see what it does. We define a Tool class that includes:

  - name (str): The name of the tool.
  - description (str): A brief description of what the tool does.
  - function (callable): The function the tool executes.
  - arguments (list): The expected input parameters.
  - outputs (str or list): The expected outputs of the tool.
  - ``__call__()``: Calls the function when the tool instance is invoked.
  - to_string(): Converts the tool’s attributes into a textual representation.
  - We could create a Tool with this class using code like the following:

    ```python
    calculator = Tool(
        name="calculator",
        description="Multiply two integers.",
        func=calculator,
        arguments=[("a", "int"), ("b", "int")],
        outputs="int"
    )
    ```

- But we can also use Python’s inspect module to retrieve all the information for us! This is what the @tool decorator does.

  ```python
  def tool(func):
      """
      A decorator that creates a Tool instance from the given function.
      """
      # Get the function signature
      signature = inspect.signature(func)

      # Extract (param_name, param_annotation) pairs for inputs
      arguments = []
      for param in signature.parameters.values():
          annotation_name = (
              param.annotation.__name__
              if hasattr(param.annotation, '__name__')
              else str(param.annotation)
          )
          arguments.append((param.name, annotation_name))

      # Determine the return annotation
      return_annotation = signature.return_annotation
      if return_annotation is inspect._empty:
          outputs = "No return annotation"
      else:
          outputs = (
              return_annotation.__name__
              if hasattr(return_annotation, '__name__')
              else str(return_annotation)
          )

      # Use the function's docstring as the description (default if None)
      description = func.__doc__ or "No description provided."

      # The function name becomes the Tool name
      name = func.__name__

      # Return a new Tool instance
      return Tool(
          name=name,
          description=description,
          func=func,
          arguments=arguments,
          outputs=outputs
      )
  ```

- Just to reiterate, with this decorator in place we can implement our tool like this:

```python
@tool
def calculator(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b

print(calculator.to_string())
```

- And we can use the Tool’s to_string method to automatically retrieve a text suitable to be used as a tool description for an LLM:

```json
Tool Name: calculator, Description: Multiply two integers., Arguments: a: int, b: int, Outputs: int
```

- The description is injected in the system prompt. Taking the example with which we started this section, here is how it would look like after replacing the tools_description:

  ```python
  system_message=""""You are an AI assistant designed to help users efficiently and accurately. Your primary goal is to provide helpful, precise, and clear responses.
  You have access to the following tools:
  Tool Name: calculator, Description: Multiply two integers., Arguments: a: int, b: int, Outputs: int
  """
  ```

#### Model Context Protocol (MCP): A Unified Tool Interface

- Model Context Protocol (MCP) is an open protocol that standardizes how applications provide tools to LLMs. MCP provides:
  - A growing list of pre-built integrations that your LLM can directly plug into
  - The flexibility to switch between LLM providers and vendors
  - Best practices for securing your data within your infrastructure

- This means that any framework implementing MCP can leverage tools defined within the protocol, eliminating the need to reimplement the same tool interface for each framework.
- Tools play a crucial role in enhancing the capabilities of AI agents.

### Understanding AI Agents through the Thought-Action-Observation Cycle

#### The Core Components

- Agents work in a continuous cycle of: thinking (Thought) → acting (Act) and observing (Observe).
- Let’s break down these actions together:
  - Thought: The LLM part of the Agent decides what the next step should be.
  - Action: The agent takes an action, by calling the tools with the associated arguments.
  - Observation: The model reflects on the response from the tool.

#### The Thought-Action-Observation Cycle

- The three components work together in a continuous loop. To use an analogy from programming, the agent uses a while loop: the loop continues until the objective of the agent has been fulfilled.
- In many Agent frameworks, the rules and guidelines are embedded directly into the system prompt, ensuring that every cycle adheres to a defined logic.
- We see here that in the System Message we defined: [System Message](image-2.png)
  - The Agent’s behavior.
  - The Tools our Agent has access to, as we described in the previous section.
  - The Thought-Action-Observation Cycle, that we bake into the LLM instructions.

- How the cycle unfolds:
  - Thought
    - Internal Reasoning: This step shows the agent breaking the problem into steps: first, gathering the necessary data.
  - Action
    - Tool Usage: The agent calls the tool to gather the data.
  - Observation
    - Feedback from the Environment: After the tool call, Agent receives an observation. This observation is then added to the prompt as additional context. It functions as real-world feedback, confirming whether the action succeeded and providing the needed details.
  - Updated Thought
    - Reflecting: With the observation in hand, Agent updates its internal reasoning.
  - Final Action
    - Agent then generates a final response formatted. This final action sends the answer back to the user, closing the loop.

- What we see in this example:
  - Agents iterate through a loop until the objective is fulfilled:
    - Agent’s process is cyclical. It starts with a thought, then acts by calling a tool, and finally observes the outcome. If the observation had indicated an error or incomplete data, Agent could have re-entered the cycle to correct its approach.

  - Tool Integration:
    - The ability to call a tool enables Agent to go beyond static knowledge and retrieve real-time data, an essential aspect of many AI Agents.

  - Dynamic Adaptation:
    - Each cycle allows the agent to incorporate fresh information (observations) into its reasoning (thought), ensuring that the final answer is well-informed and accurate.

- The interplay of Thought, Action, and Observation empowers AI agents to solve complex tasks iteratively. By understanding and applying these principles, you can design agents that not only reason about their tasks but also effectively utilize external tools to complete them, all while continuously refining their output based on environmental feedback.

### Thought: Internal Reasoning and Re-Act Approach

- The inner workings of an AI agent—its ability to reason and plan. How the agent leverages its internal dialogue to analyze information, break down complex problems into manageable steps, and decide what action to take next. Introducing the Re-Act approach, a prompting technique that encourages the model to think “step by step” before acting.

- Thoughts represent the Agent’s internal reasoning and planning processes to solve the task.
- This utilises the agent’s Large Language Model (LLM) capacity to analyze information when presented in its prompt.
- Think of it as the agent’s internal dialogue, where it considers the task at hand and strategizes its approach.
- The Agent’s thoughts are responsible for accessing current observations and decide what the next action(s) should be.
- Through this process, the agent can break down complex problems into smaller, more manageable steps, reflect on past experiences, and continuously adjust its plans based on new information.

- Here are some examples of common thoughts:

| Type of Thought | Example |
| --- | --- |
| Planning | “I need to break this task into three steps: 1) gather data, 2) analyze trends, 3) generate report” |
| Analysis | “Based on the error message, the issue appears to be with the database connection parameters” |
| Decision Making | “Given the user’s budget constraints, I should recommend the mid-tier option” |
| Problem Solving | “To optimize this code, I should first profile it to identify bottlenecks” |
| Memory Integration | “The user mentioned their preference for Python earlier, so I’ll provide examples in Python” |
| Self-Reflection | “My last approach didn’t work well, I should try a different strategy” |
| Goal Setting | “To complete this task, I need to first establish the acceptance criteria” |
| Prioritization | “The security vulnerability should be addressed before adding new features” |

- Note: In the case of LLMs fine-tuned for function-calling, the thought process is optional.

#### Re-Act Approach

- A key method is the ReAct approach, which is the concatenation of “Reasoning” (Think) with “Acting” (Act).
- ReAct is a simple prompting technique that appends “Let’s think step by step” before letting the LLM decode the next tokens.
- Indeed, prompting the model to think “step by step” encourages the decoding process toward next tokens that generate a plan, rather than a final solution, since the model is encouraged to decompose the problem into sub-tasks.
- This allows the model to consider sub-steps in more detail, which in general leads to less errors than trying to generate the final solution directly.

- [Different Types of Learning](image-3.png)