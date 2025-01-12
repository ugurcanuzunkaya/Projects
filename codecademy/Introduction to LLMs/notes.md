# Introduction to LLMs Codecademy Course - Notes

## Chatbots, Language Models and the Birth of AI

- Modern applications like ChatGPT build on decades of research in AI and natural language processing (NLP). These technologies have evolved significantly since the first chatbot, ELIZA, debuted in 1966.

- ELIZA and the “ELIZA Effect” (1966)
  - Developed at MIT by Joseph Weizenbaum. Used a simple, rule-based “script” to respond like a psychotherapist (“DOCTOR”).
  - Surprised users by appearing human.
  - “ELIZA effect”: Tendency to attribute human-like qualities to computer outputs. Refers to tendency to unconsciously attribute "humanness" to (or anthropomorphize) computer behaviours.
  - It was programmed using binary code.

- Turing Test
  - Devised by Alan Turing in his 1950 paper “Computing Machinery and Intelligence.”
  - Asks if a machine can imitate a human well enough to fool a human evaluator through text-only interaction.
  - Both ELIZA and modern models like ChatGPT can be said to pass the Turing test in various contexts.

- Birth of the Field of AI (Dartmouth, 1956)
  - A group of scientists proposed a “Summer Research Project on Artificial Intelligence,” considered a seminal moment in AI.
  - Core assumption: Every aspect of learning or intelligence can be described precisely enough for a machine to simulate it.
  - Special interest in language use, problem-solving, and self-improvement in machines.

- From Rule-Based to Neural Network–Based
  - ELIZA used fixed rules and scripts.
  - Modern systems (e.g., ChatGPT) use neural networks to capture complex statistical patterns in language.
  - This shift enables today’s sophisticated, nuanced language models.

## Deteecting Patterns in Text

- The article explores the mathematical modeling of language, beginning with historical milestones like A.A. Markov's analysis of text and Claude Shannon's prediction of letters in language. It delves into the concept of next-letter prediction, explaining how linguistic patterns and context help narrow possibilities for word formation. The field of Natural Language Processing (NLP) focuses on automating this pattern recognition process using computational models.
- The text also discusses breaking down language into smaller units—letters (unigrams), groups of letters (n-grams), words, or tokens—for easier mathematical analysis, enabling computers to predict or analyze language patterns effectively.

- Key Points
  - Historical Background
    - In 1913, A.A. Markov analyzed letters in a Russian novel, pioneering mathematical text analysis.
    - Claude Shannon expanded on this by studying letter patterns and predictability in language.

  - Next-Letter Prediction
    - Context and sentence structure help predict the next word or letter.
    - Examples include using “eru-” to predict “erupt” based on linguistic and contextual cues (e.g., “volcano”).

  - Introduction to NLP
    - NLP automates language understanding and prediction tasks.
    - It transforms text into mathematical representations for computers to analyze.
  
  - Breaking Down Language into Units
    - Unigrams: Single letters (e.g., “o,” “h”).
    - Bigrams/Trigrams: Groups of two or three letters (e.g., “oh,” “my”).
    - N-grams: General groupings of n-length letters or tokens.
    - Words: More natural units, identified by spaces.
    - Tokens: Subword units (e.g., suffixes like “-ing” or “-ed”).

  - Application
    - Language models use these units to predict or analyze linguistic patterns.
    - Tools like Google’s n-gram viewer offer statistical insights into word frequency.

##  Autoregressive Language Models

- This section introduces autoregressive language models in Natural Language Processing (NLP), which predict future text based on previous text. It highlights tasks well-suited for NLP, like translation, autocomplete, question-answering, and sentiment analysis. Autoregressive models use past word sequences to determine the next likely word. A simple approach to creating a language model involves using a text corpus to build a frequency-based lookup table, known as a count-based language model.

- Key Points
  - Applications of NLP Algorithms
    - Translation (e.g., Google Translate).
    - Autocomplete or completing letter sequences.
    - Question-answering (e.g., customer service chatbots).
    - Sentiment analysis (e.g., for content filtering).
  
  - Language Models in NLP
    - Aim to perform diverse language-related tasks.
    - Larger models could exhibit generalized intelligence akin to human thought.
    - The core question for language models: What is the next best thing to say?
  
  - Autoregressive Models
    - Predict future text based on past text sequences.
    - Operate by analyzing previously occurring words or sequences.

  - Text Corpus
    - A collection of text from multiple sources (e.g., books, articles, websites).
    - Digitally stored for analysis.

  - Count-Based Language Models
    - Simplest form of a language model.
    - Uses a lookup table to store word combinations and their frequencies.
    - Helps predict the likelihood of word sequences.

##  Count-based Autoregressive Language Models

- Count-based autoregressive language models use probabilities derived from a text corpus to predict the likelihood of specific word sequences. They calculate the probability of a sentence by chaining conditional probabilities for each word, given its preceding words. This method involves creating a lookup table that tracks word combinations and their frequencies, enabling the estimation of these probabilities.

- Key Points
  - Understanding Conditional Probability
    - `P(do | what)` represents the probability of the word "do" appearing after "what."  
    - It is calculated by dividing the frequency of "what do" by the sum of frequencies of all phrases starting with "what."

        $$
        P(do | what) = \frac{\text{Frequency of "what do"}}{\text{Total frequency of all phrases starting with "what"}}
        $$

    - Example:  
        $$
        P(do \,|\, what) = \frac{40}{40 + 16 + 16 + 8} = 0.5
        $$

  - Sentence Probability Calculation
    - The probability of a sentence (e.g., "What do I say next?") is the product of:  
        $$
        P(\text{sentence}) = P(\text{what}) \times P(\text{do} \,|\, \text{what}) \times P(\text{I} \,|\, \text{what do}) \times P(\text{say} \,|\, \text{what do I}) \times P(\text{next} \,|\, \text{what do I say})
        $$

  - Chaining Probabilities
    - Each word’s probability depends on the sequence of preceding words.  
    - For example:  
          $$ P(\text{what do}) = P(\text{what}) \times P(\text{do} \,|\, \text{what}) $$
      - Extended to calculate the entire sentence’s probability.

  - Role of Lookup Tables
    - Lookup tables store word combinations and their frequencies from a text corpus.  
    - They allow for quick probability calculations of word sequences.
  
  - Simplification
    - The example uses a small set of possibilities for clarity, but real-world corpora contain vastly larger and more complex data.  

## Generalization: From Count-based to Neural Language Models

- Count-based language models struggle with generalization, assigning zero probability to sequences not present in their training data. Neural language models overcome this limitation by leveraging word embeddings, mathematical representations of words based on their meanings and contexts. Word embeddings allow models to generalize by linking semantically related words and understanding context, even for unseen sentences. Neural networks are the most efficient tools for creating such models, enabling semantic understanding and adaptability to new data.

- Key Points
  - Limitations of Count-Based Models
    - Assign zero probability to unseen word sequences (e.g., "A lion is chasing a llama").
    - Lack the ability to generalize to new or hypothetical scenarios.

  - Generalization in Language Models
    - Refers to the model's ability to work with unseen or new data.
    - Requires understanding the meaning (semantics) of words, not just their counts.

  - Semantic Representation and Word Embeddings
    - Semantic representation connects words based on meaning and context (e.g., linking "lion" with "predator").
    - Word embeddings:
      - Transform words into numerical vectors in an abstract semantic space.
      - Words with similar meanings appear closer together in this space.
      - Handle homonyms by understanding context (e.g., “lead” in “lead pipe” vs. “lead President”).
  
  - Neural Language Models
    - Built using neural networks, which excel at creating word embeddings.
    - Enable generalization by understanding context and meaning.
    - Known as neural language models due to their reliance on neural networks.

  - Terminology Clarification
    - Generative: Ability to create data (text, images, etc.).
    - Generalization: Ability to adapt to or generate unseen data.

  - Example Application
    - A neural language model could assign a non-zero probability to "A lion is chasing a llama" by understanding the connection between "predator" and "prey," even if the specific sentence was not in its training corpus.

  - Simple image to show difference [Image1](image1.png)

##  Compression: Solving the Curse of Dimensionality

- Count-based language models face the curse of dimensionality as the size of their count tables grows exponentially with larger text corpora. Neural language models address this by compressing text data into smaller, approximate representations using model parameters (weights). While this introduces some information loss, it enables generalization, allowing models to predict unseen text by making semantic connections.

- Key Points
  - Curse of Dimensionality
    - As text corpora grow, the size of count tables expands exponentially.
      - Example: For a 100-word document, calculating probabilities of every 5-word sentence results in $ 100^5 = 10 \, \text{billion counts} $
    - Storing and processing such massive tables require significant computing power and memory.

  - Compression in Neural Language Models
    - Neural models compress large count tables into smaller sets of parameters (weights).  
    - This is akin to reducing a high-resolution image to a lower resolution, retaining essential features while reducing storage needs.  

  - Benefits and Drawbacks of Compression
    - Information Loss: Some existing text may incorrectly receive zero probabilities.  
    - Generalization: Enables models to assign non-zero probabilities to novel, unseen text by forming semantic connections.  
      - Example: The model links “lion → predator,” “predator → chasing prey,” and “llama → prey,” predicting "A lion is chasing a llama" despite it not being in the training data.  

  - Compression vs. Generalization
    - Compression and generalization are interdependent:  
      - Compression introduces the potential for generalization by finding semantic patterns in data. Zero probabilities to existing text are a trade-off for the ability to predict new text.
      - Generalization allows models to generate or predict novel text. Non-zero probabilities for unseen text are a trade-off for some information loss.

  - Significance
    - Neural models use compression to address computational limitations while enabling more robust, adaptable predictions.  

##  Neural Networks and Language Models

- The evolution of NLP and AI highlights the transition from symbolic AI, like ELIZA, to subsymbolic AI, powered by neural networks. Neural networks, inspired by biological neurons, have undergone significant development, particularly with the advent of deep learning and the availability of large datasets. The introduction of transformer architectures in 2017 revolutionized NLP, leading to the development of Generative Pre-trained Transformers (GPTs), which excel at language tasks by leveraging massive text corpora.

- Key Points
  - Symbolic AI and ELIZA
    - Symbolic AI: Early attempts at AI using rule-based systems grounded in mathematical logic.
    - ELIZA: A program that mimicked conversation by applying explicit rules and pre-scripted responses.

  - Subsymbolic AI and Neural Networks
    - Inspired by neuroscience's insights into unconscious processes.
    - Perceptron (1958): Frank Rosenblatt's model simulating a single neuron.
    - Neural networks mimic the brain by layering perceptrons to process information intelligently.

  - Resurgence of Neural Networks
    - Early 2000s: Neural networks gained popularity with the rise of big data and increased computational power.
    - Machine Learning: Algorithms that learn patterns from data for tasks like prediction and generation.
    - Deep Learning: A subset of machine learning using multi-layered neural networks for complex tasks.

  - Neural Network Architectures
    - Convolutional Neural Networks (CNNs): Best for image processing.
    - Recurrent Neural Networks (RNNs): Effective for sequential data (e.g., language translation and speech recognition).

  - Transformers: A Breakthrough in NLP
    - Introduced in 2017, transformers outperform RNNs in language-related tasks.
    - Generative Pre-trained Transformers (GPTs): Use transformer architecture to process vast text corpora and generate human-like text.

  - Significance of Transformers
    - Capture semantic patterns in text, enabling advanced language modeling.
    - Form the basis for large language models (LLMs) like GPT.

##  LLMs: Caveats and Possibilities

- Large Language Models (LLMs) build upon the foundational principles of smaller language models but achieve more sophisticated performance by training on vast amounts of data. This scaling leads to emergence, where LLMs exhibit unexpected abilities, but also introduces challenges like hallucinations, where models generate incorrect or unverifiable text. Despite efforts to mitigate hallucinations using techniques like human feedback, the issue remains inherent due to the limitations of static training data and information compression.

- Key Points
  - Core Concepts of Language Models
    - Train on text corpora to predict the next best word or token.
    - Use probability distributions and neural embeddings to preserve word meaning and context.
    - Solve issues like generalization and the curse of dimensionality through data compression.

  - Scaling LLMs
    - Larger training data increases model complexity and computational cost.
    - Compression enables generalization but introduces some degree of information loss.

  - Emergence in LLMs
    - Definition: A qualitative leap in performance resulting from quantitative scaling of training data and model size.
    - LLMs exhibit unexpected capabilities, such as:
      - Explaining jokes.
      - Creating counterfactuals.
      - Imitating specific authors’ styles.
      - Writing poetry or complex narratives.
      - Raises speculation about potential Artificial General Intelligence (AGI).

  - Hallucinations in LLMs
    - Occur when the model generates incorrect, unverifiable, or absurd information.
    - Root causes:
      - Generalization of unseen text.
      - Information loss due to compression.
      - Static nature of pre-trained models lacking real-time factual updates.

  - Factual Grounding Challenges
    - LLMs depend on the accuracy of training data and cannot inherently verify facts.
    - Lack of awareness of what they "don’t know" exacerbates errors.
    - Human feedback (e.g., reinforcement learning from human feedback) helps reduce but cannot fully eliminate hallucinations.

  - Trade-Offs of LLMs
    - Strengths: Exceptional generalization, creativity, and complex task-solving.
    - Weaknesses: Susceptibility to factual errors, inability to stay updated, and computationally intensive scaling.

## LLM Parameters: Temperature

- Temperature is a key parameter in LLMs that adjusts the sharpness of the probability distribution for next-word predictions. By tuning the temperature, users can control the balance between deterministic (predictable) and creative (random) outputs. A low temperature narrows the probability distribution, favoring high-probability outcomes, while a high temperature widens it, allowing for more novel and diverse possibilities. However, neither setting guarantees factual accuracy.

- Key Points
  - What is Temperature?
    - Controls the sharpness of the probability distribution in text generation.
    - Affects the likelihood of high-probability vs. low-probability outcomes.

  - Effects of Temperature Adjustment
    - Low Temperature:
      - Narrows the probability distribution.
      - High-probability outcomes become more likely.
      - Results are more deterministic (reliable and consistent outputs).
      - Example: "The cat chases" is favored.
    - High Temperature:
      - Widens the probability distribution.
      - Allows for more diverse and novel outcomes, including lower-probability options.
      - Results are more creative or random.
      - Example: "The cat eats mango" might become more probable.

  - Applications of Temperature
    - Low temperature: Use when seeking precise or predictable results.
    - High temperature: Use for creative writing or generating unexpected outcomes.

  - Caveats
    - High-probability outcomes (low temperature) do not guarantee factual accuracy.
    - High creativity (high temperature) may lead to amusing or incoherent results.
    - Always verify the factual correctness of outputs.

  - Additional Parameters
    - LLMs provide other parameters to adjust frequency, sampling methods, and diversity in outputs.

## Summary

- LLMs are the technology at the heart of the most recent advancements in the field of NLP. They’re the reason why chatbots come such a long way since the days of ELIZA! Some examples of popular LLMs are GPT, PaLM, Llama, BLOOM etc. These are known as base or foundational models upon which specific applications are built. For instance, the chatbot ChatGPT is built on top of GPT (version 3.5). And the chatbot developed by Google known as Bard is built on PaLM (Pathways Language Model).

- So what goes on inside a LLM when it’s prompted? Something like what’s depicted in the applet to the right! The applet shows the multiple pathways of text generation possible at each instance for the LLM. At every step, the best thing to say is chosen based on a set of probabilities generated from its training phase. Feel free to zoom in and/or scroll around the applet to view text generation in action!

- To conclude the lesson, here’s recap of all the key concepts you’ve learned about LLMs:

  - Language models are algorithmic systems trained on a corpus of text to perform a variety of tasks relating to language such as text generation, summarization, translation, etc. Large Language Models (LLMs) are trained on large amounts of text and use neural networks to learn the underlying distribution of words in text.

  - LLMs have grown in performance and popularity over the last decade due to a specific type of highly efficient neural network architecture known as the transformer. Neural networks solve the problems of lack of generalizability and the curse of dimensionality by compressing the text data into a mathematical representation.

  - Compression and generalization are the heart of the mechanism that makes LLMs powerful tools that can exhibit emergent properties. The downside to generative language models there is no guarantee of factual grounding in their outputs.

  - All autoregressive models, count-based or neural, produce outputs based on probability distributions they generate for the next best thing to say. LLM API’s have a variety of parameters to tweak these probabilities to get a desired output. We explored one such important parameter, temperature that controls for how deterministic the LLM output is.
