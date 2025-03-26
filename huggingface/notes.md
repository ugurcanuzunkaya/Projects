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
