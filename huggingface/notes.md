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
- This is what's behind models like Deepseek R1 or OpenAI's o1, which have been fine-tuned to "think before answering". These models have been trained to always include specific thinking sections (enclosed between `<think>` and `</think>` special tokens). This is not just a prompting technique like ReAct, but a training method where the model learns to generate these sections after analyzing thousands of examples that show what we expect it to do.

### Actions: Enabling the Agent to Engage with Its Environment

- We’ll cover how actions are represented (using JSON or code), the importance of the stop and parse approach, and introduce different types of agents.

- Actions are the concrete steps an AI agent takes to interact with its environment. Whether it’s browsing the web for information or controlling a physical device, each action is a deliberate operation executed by the agent.

#### Types of Agent Actions

- There are multiple types of Agents that take actions differently.

  | Type of Agent | Description |
  | --- | --- |
  | JSON Agent | The Action to take is specified in JSON format. |
  | Code Agent | The Agent writes a code block that is interpreted externally. |
  | Function-calling Agent | It is a subcategory of the JSON Agent which has been fine-tuned to generate a new message for each action. |

- Actions themselves can serve many purposes:

  | Type of Action | Description |
  | --- | --- |
  | Information Gathering | Performing web searches, querying databases, or retrieving documents. |
  | Tool Usage | Making API calls, running calculations, and executing code. |
  | Environment Interaction | Manipulating digital interfaces or controlling physical devices. |
  | Communication | Engaging with users via chat or collaborating with other agents. |

- One crucial part of an agent is the ability to STOP generating new tokens when an action is complete, and that is true for all formats of Agent: JSON, code, or function-calling. This prevents unintended output and ensures that the agent’s response is clear and precise.

- The LLM only handles text and uses it to describe the action it wants to take and the parameters to supply to the tool.

#### The Stop and Parse Approach

- One key method for implementing actions is the stop and parse approach. This method ensures that the agent’s output is structured and predictable:

1. Generation in a Structured Format:
    - The agent outputs its intended action in a clear, predetermined format (JSON or code).

2. Halting Further Generation:
    - Once the action is complete, the agent stops generating additional tokens. This prevents extra or erroneous output.

3. Parsing the Output:
    - An external parser reads the formatted action, determines which Tool to call, and extracts the required parameters.

- Machine-readable format minimizes errors and enables external tools to accurately process the agent’s command.
- Note: Function-calling agents operate similarly by structuring each action so that a designated function is invoked with the correct arguments.

#### Code Agents

- An alternative approach is using Code Agents. The idea is: instead of outputting a simple JSON object, a Code Agent generates an executable code block—typically in a high-level language like Python. [Standard LLM Agent vs CodeAct](image-4.png)

- This approach offers several advantages:
  - Expressiveness: Code can naturally represent complex logic, including loops, conditionals, and nested functions, providing greater flexibility than JSON.
  - Modularity and Reusability: Generated code can include functions and modules that are reusable across different actions or tasks.
  - Enhanced Debuggability: With a well-defined programming syntax, code errors are often easier to detect and correct.
  - Direct Integration: Code Agents can integrate directly with external libraries and APIs, enabling more complex operations such as data processing or real-time decision making.

- We learned that Actions bridge an agent’s internal reasoning and its real-world interactions by executing clear, structured tasks—whether through JSON, code, or function calls.

- This deliberate execution ensures that each action is precise and ready for external processing via the stop and parse approach. In the next section, we will explore Observations to see how agents capture and integrate feedback from their environment.

### Observe: Integrating Feedback to Reflect and Adapt

- Observations are how an Agent perceives the consequences of its actions.

- They provide crucial information that fuels the Agent’s thought process and guides future actions. They are signals from the environment—whether it’s data from an API, error messages, or system logs—that guide the next cycle of thought.

- In the observation phase, the agent:
  - Collects Feedback: Receives data or confirmation that its action was successful (or not).
  - Appends Results: Integrates the new information into its existing context, effectively updating its memory.
  - Adapts its Strategy: Uses this updated context to refine subsequent thoughts and actions.

- This iterative incorporation of feedback ensures the agent remains dynamically aligned with its goals, constantly learning and adjusting based on real-world outcomes.
- These observations can take many forms, from reading webpage text to monitoring a robot arm’s position. This can be seen like Tool “logs” that provide textual feedback of the Action execution.

  | Type of Observation | Example |
  | --- | --- |
  | System Feedback | Error messages, success notifications, status codes |
  | Data Changes | Database updates, file system modifications, state changes |
  | Environmental Data | Sensor readings, system metrics, resource usage |
  | Response Analysis | API responses, query results, computation outputs |
  | Time-based Events | Deadlines reached, scheduled tasks completed |

- How Are the Results Appended?
  - After performing an action, the framework follows these steps in order:
    - Parse the action to identify the function(s) to call and the argument(s) to use.
    - Execute the action.
    - Append the result as an Observation.

### Dummy Agent Library

- This course is framework-agnostic because we want to focus on the concepts of AI agents and avoid getting bogged down in the specifics of a particular framework.
- We will use a dummy agent library and a simple serverless API to access our LLM engine. You probably wouldn’t use these in production, but they will serve as a good starting point for understanding how agents work.

- [Dummy Agent Python File](dummy_agent.py)

- As seen in the LLM section, if we just do decoding, the model will only stop when it predicts an EOS token, and this does not happen here because this is a conversational (chat) model and we didn’t apply the chat template it expects.

- The chat method is the RECOMMENDED method to use in order to ensure a smooth transition between models.

#### Dummy Agent

- This system prompt is a bit more complex than the one we saw earlier, but it already contains:

1. Information about the tools
2. Cycle instructions (Thought → Action → Observation)

### Let's Create Our First Agent Using smolagents

- smolagents: a library that provides a framework for developing your agents with ease. smolagents is a library that focuses on codeAgent, a kind of agent that performs “Actions” through code blocks, and then “Observes” results by executing the code.

#### The Agent

- This Agent still uses the InferenceClient. You need to focus on adding new tools to the list of tools using the tools parameter of your Agent. Adding tools will give your agent new capabilities

#### The System Prompt

- The agent’s system prompt is stored in a seperate prompts.yaml file. This file contains predefined instructions that guide the agent’s behavior. Storing prompts in a YAML file allows for easy customization and reuse across different agents or use cases.
- Your Goal is to get familiar with the Space and the Agent. Currently, the agent in the template does not use any tools, so try to provide it with some of the pre-made ones or even make some new tools yourself!

## Bonus Unit 1: Fine-Tuning An LLM for Function Calling

### Introduction

- You’ll learn to fine-tune a Large Language Model (LLM) for function calling.
- In terms of LLMs, function calling is quickly becoming a must-know technique.
- The idea is, rather than relying only on prompt-based approaches like we did in Unit 1, function calling trains your model to take actions and interpret observations during the training phase, making your AI more robust.

- What You’ll Learn
  - Function Calling
    - How modern LLMs structure their conversations effectively letting them trigger Tools.

  - LoRA (Low-Rank Adaptation)
    - A lightweight and efficient fine-tuning method that cuts down on computational and storage overhead. LoRA makes training large models faster, cheaper, and easier to deploy.

  - The Thought → Act → Observe Cycle in Function Calling models
    - A simple but powerful approach for structuring how your model decides when (and how) to call functions, track intermediate steps, and interpret the results from external Tools or APIs.

  - New Special Tokens
    - We’ll introduce special markers that help the model distinguish between:
      - Internal “chain-of-thought” reasoning
      - Outgoing function calls
      - Responses coming back from external tools

- By the end of this bonus unit, you’ll be able to:
  - Understand the inner working of APIs when it comes to Tools.
  - Fine-tune a model using the LoRA technique.
  - Implement and modify the Thought → Act → Observe cycle to create robust and maintainable Function-calling workflows.
  - Design and utilize special tokens to seamlessly separate the model’s internal reasoning from its external actions.
- And you’ll have fine-tuned your own model to do function calling.

### What is Function Calling?

- Function-calling is a way for an LLM to take actions on its environment. It was first introduced in GPT-4, and was later reproduced in other models.

- Just like the tools of an Agent, function-calling gives the model the capacity to take an action on its environment. However, the function calling capacity is learned by the model, and relies less on prompting than other agents techniques.

- During Unit 1, the Agent didn’t learn to use the Tools, we just provided the list, and we relied on the fact that the model was able to generalize on defining a plan using these Tools.

- While here, with function-calling, the Agent is fine-tuned (trained) to use Tools.

- How does the model “learn” to take an action?
  - In Unit 1, we explored the general workflow of an agent. Once the user has given some tools to the agent and prompted it with a query, the model will cycle through:
    - Think : What action(s) do I need to take in order to fulfill the objective.
    - Act : Format the action with the correct parameter and stop the generation.
    - Observe : Get back the result from the execution.

- In a “typical” conversation with a model through an API, the conversation will alternate between user and assistant messages like this:

```python
conversation = [
    {"role": "user", "content": "I need help with my order"},
    {"role": "assistant", "content": "I'd be happy to help. Could you provide your order number?"},
    {"role": "user", "content": "It's ORDER-123"},
]
```

- Function-calling brings new roles to the conversation!
  - One new role for an Action
  - One new role for an Observation

- There’s a new role for function calls? Yes and no, in this case and in a lot of other APIs, the model formats the action to take as an “assistant” message. The chat template will then represent this as special tokens for function-calling.
  - `[AVAILABLE_TOOLS]` – Start the list of available tools
  - `[/AVAILABLE_TOOLS]` – End the list of available tools
  - `[TOOL_CALLS]` – Make a call to a tool (i.e., take an “Action”)
  - `[TOOL_RESULTS]` – “Observe” the result of the action
  - `[/TOOL_RESULTS]` – End of the observation (i.e., the model can decode again)

### Let’s Fine-Tune Your Model for Function-Calling

- How do we train our model for function-calling? We need data

- A model training process can be divided into 3 steps:
  - The model is pre-trained on a large quantity of data. The output of that step is a pre-trained model.For instance, google/gemma-2-2b. It’s a base model and only knows how to predict the next token without strong instruction following capabilities.
  - To be useful in a chat context, the model then needs to be fine-tuned to follow instructions. In this step, it can be trained by model creators, the open-source community, you, or anyone.
  - The model can then be aligned to the creator’s preferences.
- Starting from the pre-trained model would require more training in order to learn instruction following, chat AND function-calling.
- By starting from the instruction-tuned model, we minimize the amount of information that our model needs to learn.

#### LoRA (Low-Rank Adaptation of Large Language Models)

- LoRA is a popular and lightweight training technique that significantly reduces the number of trainable parameters.
- It works by inserting a smaller number of new weights as an adapter into the model to train. This makes training with LoRA much faster, memory-efficient, and produces smaller model weights (a few hundred MBs), which are easier to store and share. [LoRA](https://cdn-lfs-us-1.hf.co/repos/45/f4/45f48d5b3577034b76ee728dfe60afca3d0aa70790fda3e706eeb9276d8d5331/1eabf1d1859a8fa93a90428330b2546e051994fb3fb7c9df551094675d6872ed?response-content-disposition=inline%3B+filename*%3DUTF-8%27%27blog_multi-lora-serving_LoRA.gif%3B+filename%3D%22blog_multi-lora-serving_LoRA.gif%22%3B&response-content-type=image%2Fgif&Expires=1743792717&Policy=eyJTdGF0ZW1lbnQiOlt7IkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0Mzc5MjcxN319LCJSZXNvdXJjZSI6Imh0dHBzOi8vY2RuLWxmcy11cy0xLmhmLmNvL3JlcG9zLzQ1L2Y0LzQ1ZjQ4ZDViMzU3NzAzNGI3NmVlNzI4ZGZlNjBhZmNhM2QwYWE3MDc5MGZkYTNlNzA2ZWViOTI3NmQ4ZDUzMzEvMWVhYmYxZDE4NTlhOGZhOTNhOTA0MjgzMzBiMjU0NmUwNTE5OTRmYjNmYjdjOWRmNTUxMDk0Njc1ZDY4NzJlZD9yZXNwb25zZS1jb250ZW50LWRpc3Bvc2l0aW9uPSomcmVzcG9uc2UtY29udGVudC10eXBlPSoifV19&Signature=HaC9m1wjcFyTj7KbTbdGg7Syq1G%7EoI63dA9PiasDCUVPGzEhRPx6ATx4BKPCe5xWLWe35N%7EOPW%7E4Li4Tzo3fwxnvCjJACkY9k4-w%7Em7c%7EbPpj4NTS7VIW4tUHne4C6rosoYLTKywAUofh0PIJ5r2fAi2idfeI7NKHNowecLdCLX-%7EQw6XE49G9LYEnjTO28-zOn2A2JUQRpzcnY5pF8OSgHHf62bp%7EVsmNTfU2aMMNBLIRzgGV-ClgfxPaLaq9XKpblqq8ph6CCBCEvvmtwcoAQv2CucJqyzrfe5kQF7dHUUU6O9Ez9giO8SjKA0fF4XgDazA1ruP1TZOis4qE4-Nw__&Key-Pair-Id=K24J24Z295AEI9)

- LoRA works by adding pairs of rank decomposition matrices to Transformer layers, typically focusing on linear layers. During training, we will “freeze” the rest of the model and will only update the weights of those newly added adapters.

- By doing so, the number of parameters that we need to train drops considerably as we only need to update the adapter’s weights.

- During inference, the input is passed into the adapter and the base model, or these adapter weights can be merged with the base model, resulting in no additional latency overhead.

- LoRA is particularly useful for adapting large language models to specific tasks or domains while keeping resource requirements manageable. This helps reduce the memory required to train a model.

### Conclusion

- You’ve just mastered understanding function-calling and how to fine-tune your model to do function-calling! If we have one piece of advice now, it’s to try to fine-tune different models. The best way to learn is by trying.

## Unit 2: Introduction to Agentic Frameworks

### When to Use an Agentic Framework

- An agentic framework is not always needed when building an application around LLMs. They provide flexibility in the workflow to efficiently solve a specific task, but they’re not always necessary.

- Sometimes, predefined workflows are sufficient to fulfill user requests, and there is no real need for an agentic framework. If the approach to build an agent is simple, like a chain of prompts, using plain code may be enough. The advantage is that the developer will have full control and understanding of their system without abstractions.

- However, when the workflow becomes more complex, such as letting an LLM call functions or using multiple agents, these abstractions start to become helpful.

- Considering these ideas, we can already identify the need for some features:

  - An LLM engine that powers the system.
  - A list of tools the agent can access.
  - A parser for extracting tool calls from the LLM output.
  - A system prompt synced with the parser.
  - A memory system.
  - Error logging and retry mechanisms to control LLM mistakes. We’ll explore how these topics are resolved in various frameworks, including smolagents, LlamaIndex, and LangGraph.

- Agentic Frameworks Units

| Framework | Description |
| --- | --- |
| smolagents | Agents framework developed by Hugging Face. |
| Llama-Index | End-to-end tooling to ship a context-augmented AI agent to production |
| LangGraph | Agents allowing stateful orchestration of agents |

## Unit 2.1: smolagents

### Introduction to smolagents

#### Module Overview

- We’ll explore critical agent types, including code agents designed for software development tasks, tool calling agents for creating modular, function-driven workflows, and retrieval agents that access and synthesize information.
- Additionally, we’ll cover the orchestration of multiple agents as well as the integration of vision capabilities and web browsing, which unlock new possibilities for dynamic and context-aware applications.
- Our agents will be able to search for data, execute code, and interact with web pages. You will also learn how to combine multiple agents to create more powerful systems.

- Contents
  - Why Use smolagents
    - smolagents is one of the many open-source agent frameworks available for application development. Alternative options include LlamaIndex and LangGraph, which are also covered in other modules in this course. smolagents offers several key features that might make it a great fit for specific use cases, but we should always consider all options when selecting a framework. We’ll explore the advantages and drawbacks of using smolagents, helping you make an informed decision based on your project’s requirements.
  - CodeAgents
    - CodeAgents are the primary type of agent in smolagents. Instead of generating JSON or text, these agents produce Python code to perform actions. This module explores their purpose, functionality, and how they work, along with hands-on examples to showcase their capabilities.
  - ToolCallingAgents
    - ToolCallingAgents are the second type of agent supported by smolagents. Unlike CodeAgents, which generate Python code, these agents rely on JSON/text blobs that the system must parse and interpret to execute actions. This module covers their functionality, their key differences from CodeAgents, and it provides an example to illustrate their usage.
  - Retrieval Agents
    - Retrieval agents allow models access to knowledge bases, making it possible to search, synthesize, and retrieve information from multiple sources. They leverage vector stores for efficient retrieval and implement Retrieval-Augmented Generation (RAG) patterns. These agents are particularly useful for integrating web search with custom knowledge bases while maintaining conversation context through memory systems. This module explores implementation strategies, including fallback mechanisms for robust information retrieval.
  - Multi-Agent Systems
    - Orchestrating multiple agents effectively is crucial for building powerful, multi-agent systems. By combining agents with different capabilities—such as a web search agent with a code execution agent—you can create more sophisticated solutions. This module focuses on designing, implementing, and managing multi-agent systems to maximize efficiency and reliability.
  - Vision and Browser Agents
    - Vision agents extend traditional agent capabilities by incorporating Vision-Language Models (VLMs), enabling them to process and interpret visual information. This module explores how to design and integrate VLM-powered agents, unlocking advanced functionalities like image-based reasoning, visual data analysis, and multimodal interactions. We will also use vision agents to build a browser agent that can browse the web and extract information from it.
- Resources
  - [smolagents Documentation](https://huggingface.co/docs/smolagents) - Official docs for the smolagents library
  - [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) - Research paper on agent architectures
  - [Agent Guidelines](https://huggingface.co/docs/smolagents/tutorials/building_good_agents) - Best practices for building reliable agents
  - [LangGraph Agents](https://langchain-ai.github.io/langgraph/) - Additional examples of agent implementations
  - [Function Calling Guide](https://platform.openai.com/docs/guides/function-calling) - Understanding function calling in LLMs
  - [RAG Best Practices](https://www.pinecone.io/learn/retrieval-augmented-generation/) - Guide to implementing effective RAG

### Why Use smolagents

- smolagents is a simple yet powerful framework for building AI agents. It provides LLMs with the agency to interact with the real world, such as searching or generating images.
- AI agents are programs that use LLMs to generate ‘thoughts’ based on ‘observations’ to perform ‘actions’.

#### Key Advantages of smolagents

- Simplicity: Minimal code complexity and abstractions, to make the framework easy to understand, adopt and extend
- Flexible LLM Support: Works with any LLM through integration with Hugging Face tools and external APIs
- Code-First Approach: First-class support for Code Agents that write their actions directly in code, removing the need for parsing and simplifying tool calling
- HF Hub Integration: Seamless integration with the Hugging Face Hub, allowing the use of Gradio Spaces as tools

#### When to Use smolagents

- With these advantages in mind, when should we use smolagents over other frameworks?
- smolagents is ideal when:
  - You need a lightweight and minimal solution.
  - You want to experiment quickly without complex configurations.
  - Your application logic is straightforward.

#### Code vs. JSON Actions

- Unlike other frameworks where agents write actions in JSON, smolagents focuses on tool calls in code, simplifying the execution process. This is because there’s no need to parse the JSON in order to build code that calls the tools: the output can be executed directly. [Standard LLM Agent vs CodeAct](image-6.png)

#### Agent Types in smolagents

- Agents in smolagents operate as multi-step agents.
- Each MultiStepAgent performs:
  - One thought
  - One tool call and execution
  - In addition to using CodeAgent as the primary type of agent, smolagents also supports ToolCallingAgent, which writes tool calls in JSON.
- In smolagents, tools are defined using `@tool` decorator wrapping a python function or the Tool class.

#### Model Integration in smolagents

- `smolagents` supports flexible LLM integration, allowing you to use any callable model that meets [certain criteria](https://huggingface.co/docs/smolagents/main/en/reference/models). The framework provides several predefined classes to simplify model connections:

  - [TransformersModel](https://huggingface.co/docs/smolagents/main/en/reference/models#smolagents.TransformersModel): Implements a local `transformers` pipeline for seamless integration.
  - [HfApiModel](https://huggingface.co/docs/smolagents/main/en/reference/models#smolagents.HfApiModel): Supports [serverless inference](https://huggingface.co/docs/huggingface_hub/main/en/guides/inference) calls through [Hugging Face's infrastructure](https://huggingface.co/docs/api-inference/index), or via a growing number of [third-party inference providers](https://huggingface.co/docs/huggingface_hub/main/en/guides/inference#supported-providers-and-tasks).
  - [LiteLLMModel](https://huggingface.co/docs/smolagents/main/en/reference/models#smolagents.LiteLLMModel): Leverages [LiteLLM](https://www.litellm.ai/) for lightweight model interactions.
  - [OpenAIServerModel](https://huggingface.co/docs/smolagents/main/en/reference/models#smolagents.OpenAIServerModel): Connects to any service that offers an OpenAI API interface.
  - [AzureOpenAIServerModel](https://huggingface.co/docs/smolagents/main/en/reference/models#smolagents.AzureOpenAIServerModel): Supports integration with any Azure OpenAI deployment.

- This flexibility ensures that developers can choose the model and service most suitable for their specific use cases, and allows for easy experimentation.

- [smolagents Blog](https://huggingface.co/blog/smolagents) - Introduction to smolagents and code interactions

### Building Agents That Use Code

- Code agents are the default agent type in smolagents. They generate Python tool calls to perform actions, achieving action representations that are efficient, expressive, and accurate. Their streamlined approach reduces the number of required actions, simplifies complex operations, and enables reuse of existing code functions. smolagents provides a lightweight framework for building code agents, implemented in approximately 1,000 lines of code.

#### Why Code Agents?

- In a multi-step agent process, the LLM writes and executes actions, typically involving external tool calls. Traditional approaches use a JSON format to specify tool names and arguments as strings, which the system must parse to determine which tool to execute. However, research shows that tool-calling LLMs work more effectively with code directly.

- Writing actions in code rather than JSON offers several key advantages:
  - Composability: Easily combine and reuse actions
  - Object Management: Work directly with complex structures like images
  - Generality: Express any computationally possible task
  - Natural for LLMs: High-quality code is already present in LLM training data

#### How Does a Code Agent Work?

- [CodeAgent works](image-7.png)
- The diagram above illustrates how CodeAgent.run() operates, following the ReAct framework we mentioned in Unit 1. The main abstraction for agents in smolagents is a MultiStepAgent, which serves as the core building block. CodeAgent is a special kind of MultiStepAgent.
- A CodeAgent performs actions through a cycle of steps, with existing variables and knowledge being incorporated into the agent’s context, which is kept in an execution log:
  1. The system prompt is stored in a SystemPromptStep, and the user query is logged in a TaskStep.
  2. Then, the following while loop is executed:
      1. Method agent.write_memory_to_messages() writes the agent’s logs into a list of LLM-readable chat messages.
      2. These messages are sent to a Model, which generates a completion.
      3. The completion is parsed to extract the action, which, in our case, should be a code snippet since we’re working with a CodeAgent.
      4. The action is executed.
      5. The results are logged into memory in an ActionStep.

- At the end of each step, if the agent includes any function calls (in agent.step_callback), they are executed.

#### Selecting a Playlist for the Party Using smolagents

- Music is an essential part of a successful party! Alfred needs some help selecting the playlist. Luckily, smolagents has got us covered! We can build an agent capable of searching the web using DuckDuckGo. To give the agent access to this tool, we include it in the tool list when creating the agent.

- [smolagents Playlist Example](building_agents.py)

- When you run this example, the output will display a trace of the workflow steps being executed.

#### Using a Custom Tool to Prepare the Menu

- Now that we have selected a playlist, we need to organize the menu for the guests. Again, Alfred can take advantage of smolagents to do so. Here, we use the @tool decorator to define a custom function that acts as a tool.
- The agent will run for a few steps until finding the answer. Precising allowed values in the docstring helps direct agent to occasion argument values which exist and limit hallucinations.

#### Using Python Imports Inside the Agent

- Alfred needs to calculate when everything would be ready if he started preparing now, in case they need assistance from other superheroes.
- smolagents specializes in agents that write and execute Python code snippets, offering sandboxed execution for security. Code execution has strict security measures - imports outside a predefined safe list are blocked by default. However, you can authorize additional imports by passing them as strings in additional_authorized_imports.
- When creating the agent, we’ll use additional_authorized_imports to allow for importing the datetime module.
- These examples are just the beginning of what you can do with code agents, and we’re already starting to see their utility for preparing the party.
- In summary, smolagents specializes in agents that write and execute Python code snippets, offering sandboxed execution for security. It supports both local and API-based language models, making it adaptable to various development environments.

#### Sharing Our Custom Party Preparator Agent to the Hub

- The smolagents library makes this possible by allowing you to share a complete agent with the community and download others for immediate use.
- What’s also exciting is that shared agents are directly available as Hugging Face Spaces, allowing you to interact with them in real-time.
- [smolagents Party Preparator](building_agents2.py)

#### Inspecting Our Party Preparator Agent with OpenTelemetry and Langfuse

- As Alfred fine-tunes the Party Preparator Agent, he’s growing weary of debugging its runs. Agents, by nature, are unpredictable and difficult to inspect. But since he aims to build the ultimate Party Preparator Agent and deploy it in production, he needs robust traceability for future monitoring and analysis.
- Once again, smolagents comes to the rescue! It embraces the OpenTelemetry standard for instrumenting agent runs, allowing seamless inspection and logging. With the help of Langfuse and the SmolagentsInstrumentor, Alfred can easily track and analyze his agent’s behavior.
- Alfred is ready to initialize the SmolagentsInstrumentor and start tracking his agent’s performance.
- Alfred is now connected 🔌! The runs from smolagents are being logged in Langfuse, giving him full visibility into the agent’s behavior. With this setup, he’s ready to revisit previous runs and refine his Party Preparator Agent even further.
- Alfred can now access these logs [here](https://cloud.langfuse.com/project/cm7bq0abj025rad078ak3luwi/traces/995fc019255528e4f48cf6770b0ce27b?timestamp=2025-02-19T10%3A28%3A36.929Z) to review and analyze them.  

Actually, a minor error occured during execution. Can you spot it in the logs? Try to track how the agent handles it and still returns a valid answer. <a href="https://cloud.langfuse.com/project/cm7bq0abj025rad078ak3luwi/traces/995fc019255528e4f48cf6770b0ce27b?timestamp=2025-02-19T10%3A28%3A36.929Z&observation=80ca57ace4f69b52">Here</a> is the direct link to the error if you want to verify your answer. Of course the error has been fixed in the meantime, more details can be found in this <a href="https://cloud.langfuse.com/project/cm7bq0abj025rad078ak3luwi/traces/995fc019255528e4f48cf6770b0ce27b?timestamp=2025-02-19T10%3A28%3A36.929Z&observation=80ca57ace4f69b52">issue</a>.

Meanwhile, the [suggested playlist](https://open.spotify.com/playlist/0gZMMHjuxMrrybQ7wTMTpw) sets the perfect vibe for the party preparations. Cool, right? 🎶  

### Writing actions as code snippets or JSON blobs

- Tool Calling Agents are the second type of agent available in smolagents. Unlike Code Agents that use Python snippets, these agents use the built-in tool-calling capabilities of LLM providers to generate tool calls as JSON structures. This is the standard approach used by OpenAI, Anthropic, and many other providers.
- While smolagents primarily focuses on CodeAgents since they perform better overall, ToolCallingAgents can be effective for simple systems that don’t require variable handling or complex tool calls.

#### How Do Tool Calling Agents Work?

- Tool Calling Agents follow the same multi-step workflow as Code Agents. The key difference is in how they structure their actions: instead of executable code, they generate JSON objects that specify tool names and arguments. The system then parses these instructions to execute the appropriate tools.

##### Example: Running a Tool Calling Agent

- Let’s revisit the previous example where Alfred started party preparations, but this time we’ll use a ToolCallingAgent to highlight the difference. We’ll build an agent that can search the web using DuckDuckGo, just like in our Code Agent example. The only difference is the agent type - the framework handles everything else.
- [smolagents Party Preparator ToolCallingAgent](building_agents3.py)
- The agent generates a structured tool call that the system processes to produce the output, rather than directly executing code like a CodeAgent. Now that we understand both agent types, we can choose the right one for our needs.

### Tools

- In smolagents, tools are treated as functions that an LLM can call within an agent system. To interact with a tool, the LLM needs an interface description with these key components:
  - Name: What the tool is called
  - Tool description: What the tool does
  - Input types and descriptions: What arguments the tool accepts
  - Output type: What the tool returns
- For instance, while preparing for a party at Wayne Manor, Alfred needs various tools to gather information - from searching for catering services to finding party theme ideas. Here’s how a simple search tool interface might look:
  - Name: web_search
  - Tool description: Searches the web for specific queries
  - Input: query (string) - The search term to look up
  - Output: String containing the search results
- By using these tools, Alfred can make informed decisions and gather all the information needed for planning the perfect party. [How a tool call is managed](https://cdn-lfs.hf.co/datasets/huggingface/documentation-images/445679be1266aa1df3cb0ee708d0737348828e871f3d840685e0ce4ed3feee3a?response-content-disposition=inline%3B+filename*%3DUTF-8%27%27Agent_ManimCE.gif%3B+filename%3D%22Agent_ManimCE.gif%22%3B&response-content-type=image%2Fgif&Expires=1743967856&Policy=eyJTdGF0ZW1lbnQiOlt7IkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0Mzk2Nzg1Nn19LCJSZXNvdXJjZSI6Imh0dHBzOi8vY2RuLWxmcy5oZi5jby9kYXRhc2V0cy9odWdnaW5nZmFjZS9kb2N1bWVudGF0aW9uLWltYWdlcy80NDU2NzliZTEyNjZhYTFkZjNjYjBlZTcwOGQwNzM3MzQ4ODI4ZTg3MWYzZDg0MDY4NWUwY2U0ZWQzZmVlZTNhP3Jlc3BvbnNlLWNvbnRlbnQtZGlzcG9zaXRpb249KiZyZXNwb25zZS1jb250ZW50LXR5cGU9KiJ9XX0_&Signature=B0eNi-7ZKQNk5TwQYlWz7ttlNdQaPRKH7gHhj4mDimjv2%7EEIUZ%7EhwsXlo0AyOPy96s6hrTf%7Ekq-6ISWtj1I7Yvj6AEaaXuYtT86vr7f3CpzQI93%7EzY4ajKY0IOGABYacsoDfCpI1py33mFxx5-SmZYH34hA%7E7ZtA5QvzRba9WjBP6t%7EheAyOAiyrtjHenlnjP%7EIzYs1GCfAXNGOFESJ4I0Kh2US0cGuUj7fgjt42B8j8ZrDaWRIt8H%7EAwRrln6z7BytMgKbIOsM0ho94tFo96Mjv2FXHvit7UR4JzQYIup8ZKLttglWhSFPyDewWnGKVZj6nl9-wjxjJiQFteby0fw__&Key-Pair-Id=K3RPWS32NSSJCE)

#### Tool Creation Methods

- In smolagents, tools can be defined in two ways:
  - Using the @tool decorator for simple function-based tools
  - Creating a subclass of Tool for more complex functionality

##### The @tool Decorator

- The @tool decorator is the recommended way to define simple tools. Under the hood, smolagents will parse basic information about the function from Python. So if you name your function clearly and write a good docstring, it will be easier for the LLM to use.
- Using this approach, we define a function with:
  - A clear and descriptive function name that helps the LLM understand its purpose.
  - Type hints for both inputs and outputs to ensure proper usage.
  - A detailed description, including an Args: section where each argument is explicitly described. These descriptions provide valuable context for the LLM, so it’s important to write them carefully.

###### Generating a tool that retrieves the highest-rated catering

- Let’s imagine that Alfred has already decided on the menu for the party, but now he needs help preparing food for such a large number of guests. To do so, he would like to hire a catering service and needs to identify the highest-rated options available. Alfred can leverage a tool to search for the best catering services in his area.
- [smolagents Catering Tool](building_agents4.py)

##### Defining a Tool as a Python Class

- This approach involves creating a subclass of Tool. For complex tools, we can implement a class instead of a Python function. The class wraps the function with metadata that helps the LLM understand how to use it effectively. In this class, we define:
  - name: The tool’s name.
  - description: A description used to populate the agent’s system prompt.
  - inputs: A dictionary with keys type and description, providing information to help the Python interpreter process inputs.
  - output_type: Specifies the expected output type.
  - forward: The method containing the inference logic to execute.

###### Generating a tool to generate ideas about the superhero-themed party

- Alfred’s party at the mansion is a superhero-themed event, but he needs some creative ideas to make it truly special. As a fantastic host, he wants to surprise the guests with a unique theme. To do this, he can use an agent that generates superhero-themed party ideas based on a given category. This way, Alfred can find the perfect party theme to wow his guests.

#### Default Toolbox

- smolagents comes with a set of pre-built tools that can be directly injected into your agent. The default toolbox includes:
  - PythonInterpreterTool
  - FinalAnswerTool
  - UserInputTool
  - DuckDuckGoSearchTool
  - GoogleSearchTool
  - VisitWebpageTool

#### Sharing and Importing Tools

- One of the most powerful features of smolagents is its ability to share custom tools on the Hub and seamlessly integrate tools created by the community. This includes connecting with HF Spaces and LangChain tools, significantly enhancing Alfred’s ability to orchestrate an unforgettable party at Wayne Manor.

##### Sharing a Tool to the Hub

- Sharing your custom tool with the community is easy! Simply upload it to your Hugging Face account using the `push_to_hub()` method.

##### Importing a Tool from the Hub

- You can easily import tools created by other users using the load_tool() function. For example, Alfred might want to generate a promotional image for the party using AI. Instead of building a tool from scratch, he can leverage a predefined one from the community.

##### Importing a Hugging Face Space as a Tool

- You can also import a HF Space as a tool using Tool.from_space(). This opens up possibilities for integrating with thousands of spaces from the community for tasks from image generation to data analysis. The tool will connect with the spaces Gradio backend using the gradio_client, so make sure to install it via pip if you don’t have it already.

##### Importing a LangChain Tool

- You can easily load LangChain tools using the `Tool.from_langchain()` method. Alfred, ever the perfectionist, is preparing for a spectacular superhero night at Wayne Manor while the Waynes are away. To make sure every detail exceeds expectations, he taps into LangChain tools to find top-tier entertainment ideas. By using `Tool.from_langchain()`, Alfred effortlessly adds advanced search functionalities to his smolagent, enabling him to discover exclusive party ideas and services with just a few commands.

##### Importing a tool collection from any MCP server

- smolagents also allows importing tools from the hundreds of MCP servers available on glama.ai or smithery.ai.

### Building Agentic RAG (Retrieval-Augmented Generation) Systems

- Retrieval Augmented Generation (RAG) systems combine the capabilities of data retrieval and generation models to provide context-aware responses. For example, a user’s query is passed to a search engine, and the retrieved results are given to the model along with the query. The model then generates a response based on the query and retrieved information.
- Agentic RAG (Retrieval-Augmented Generation) extends traditional RAG systems by combining autonomous agents with dynamic knowledge retrieval.
- While traditional RAG systems use an LLM to answer queries based on retrieved data, agentic RAG enables intelligent control of both retrieval and generation processes, improving efficiency and accuracy.
- Traditional RAG systems face key limitations, such as relying on a single retrieval step and focusing on direct semantic similarity with the user’s query, which may overlook relevant information.
- Agentic RAG addresses these issues by allowing the agent to autonomously formulate search queries, critique retrieved results, and conduct multiple retrieval steps for a more tailored and comprehensive output.

#### Basic Retrieval with DuckDuckGo

- Let’s build a simple agent that can search the web using DuckDuckGo. This agent will retrieve information and synthesize responses to answer queries. With Agentic RAG, Alfred’s agent can:
  - Search for latest superhero party trends
  - Refine results to include luxury elements
  - Synthesize information into a complete plan
- [smolagents RAG Example](building_rag_agents.py)
- The agent follows this process:
  - Analyzes the Request: Alfred’s agent identifies the key elements of the query—luxury superhero-themed party planning, with focus on decor, entertainment, and catering.
  - Performs Retrieval: The agent leverages DuckDuckGo to search for the most relevant and up-to-date information, ensuring it aligns with Alfred’s refined preferences for a luxurious event.
  - Synthesizes Information: After gathering the results, the agent processes them into a cohesive, actionable plan for Alfred, covering all aspects of the party.
  - Stores for Future Reference: The agent stores the retrieved information for easy access when planning future events, optimizing efficiency in subsequent tasks.

#### Custom Knowledge Base Tool

- For specialized tasks, a custom knowledge base can be invaluable. Let’s create a tool that queries a vector database of technical documentation or specialized knowledge. Using semantic search, the agent can find the most relevant information for Alfred’s needs.
- A vector database stores numerical representations (embeddings) of text or other data, created by machine learning models. It enables semantic search by identifying similar meanings in high-dimensional space.
- This approach combines predefined knowledge with semantic search to provide context-aware solutions for event planning. With specialized knowledge access, Alfred can perfect every detail of the party.
- In this example, we’ll create a tool that retrieves party planning ideas from a custom knowledge base. We’ll use a BM25 retriever to search the knowledge base and return the top results, and RecursiveCharacterTextSplitter to split the documents into smaller chunks for more efficient search.
- This enhanced agent can:
  - First check the documentation for relevant information
  - Combine insights from the knowledge base
  - Maintain conversation context in memory

#### Enhanced Retrieval Capabilities

- When building agentic RAG systems, the agent can employ sophisticated strategies like:
  - Query Reformulation: Instead of using the raw user query, the agent can craft optimized search terms that better match the target documents
  - Multi-Step Retrieval: The agent can perform multiple searches, using initial results to inform subsequent queries
  - Source Integration: Information can be combined from multiple sources like web search and local documentation
  - Result Validation: Retrieved content can be analyzed for relevance and accuracy before being included in responses
- Effective agentic RAG systems require careful consideration of several key aspects. The agent should select between available tools based on the query type and context. Memory systems help maintain conversation history and avoid repetitive retrievals. Having fallback strategies ensures the system can still provide value even when primary retrieval methods fail. Additionally, implementing validation steps helps ensure the accuracy and relevance of retrieved information.

### Multi-Agent Systems

- Multi-agent systems enable specialized agents to collaborate on complex tasks, improving modularity, scalability, and robustness. Instead of relying on a single agent, tasks are distributed among agents with distinct capabilities.
- In smolagents, different agents can be combined to generate Python code, call external tools, perform web searches, and more. By orchestrating these agents, we can create powerful workflows.
- A typical setup might include:
  - A Manager Agent for task delegation
  - A Code Interpreter Agent for code execution
  - A Web Search Agent for information retrieval

- The diagram below illustrates a simple multi-agent architecture where a Manager Agent coordinates a Code Interpreter Tool and a Web Search Agent, which in turn utilizes tools like the DuckDuckGoSearchTool and VisitWebpageTool to gather relevant information. [Diagram Multi-Agent Architecture](image-8.png)

#### Multi-Agent Systems in Action

- A multi-agent system consists of multiple specialized agents working together under the coordination of an Orchestrator Agent. This approach enables complex workflows by distributing tasks among agents with distinct roles.
- For example, a Multi-Agent RAG system can integrate:
  - A Web Agent for browsing the internet.
  - A Retriever Agent for fetching information from knowledge bases.
  - An Image Generation Agent for producing visuals.

- All of these agents operate under an orchestrator that manages task delegation and interaction.
