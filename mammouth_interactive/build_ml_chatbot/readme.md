# Chatbot with TFLearn and NLTK

This project builds and trains a simple chatbot using a Neural Network (DNN) based on TFLearn (a high-level TensorFlow wrapper) and natural language processing (NLP) techniques via NLTK.

## Features

- **Intent-based Responses**: The chatbot identifies user queries by their "intent" and provides responses defined in a `data.json` file.
- **Data Preprocessing**: Automatic tokenization, stemming, and bag-of-words encoding.
- **Model Training & Persistence**: Train a neural network model to understand patterns in user input. The model is saved for future use, so subsequent runs can skip re-training if the model file exists.
- **NLTK Data Management**: Checks for essential NLTK data (punkt tokenizer and stopwords) and downloads them only if necessary.

## Requirements

- **Python 3.6+**
- **pip** or **conda** package manager

## Dependencies

- `tensorflow` (Compatible with TFLearn; check TFLearn docs for which TF version to install)
- `tflearn`
- `nltk`
- `numpy`
- `json` (standard library)
- `os` (standard library)
- `random` (standard library)

Example installation (assuming a virtual environment and Python 3.9+):

```bash
pip install tflearn tensorflow numpy nltk
```

## Setup

1. **Clone the repository** (or download the project files):

    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```

2. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

    *(Create a `requirements.txt` file if not already present. Otherwise, install packages individually.)*

3. **Ensure NLTK data**:  
   The script checks for `punkt` and `stopwords` and downloads them if not found. No manual step required unless you wish to pre-download:

   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

4. **Prepare `data.json`**:  
   Provide a `data.json` file in the following format:

   ```json
   {
       "intents": [
           {
               "tag": "greeting",
               "patterns": [
                   "Hi", "Hello", "How are you?"
               ],
               "responses": [
                   "Hello there!", "Hi! How can I help?"
               ]
           },
           {
               "tag": "goodbye",
               "patterns": [
                   "Bye", "See you later", "Goodbye"
               ],
               "responses": [
                   "Bye!", "Have a great day!"
               ]
           }
       ]
   }
   ```

   Adjust with your own intents, patterns, and responses.

## Running the Project

To run the chatbot script:

```bash
python chatbot.py
```

If the model has never been trained or the model file is missing, it will:

- Load and preprocess the data.
- Train the DNN model.
- Save the trained model.

If the model already exists:

- It will skip the training part.
- Load the existing model.
- Immediately provide responses to user queries.

## Interacting with the Chatbot

- After running the script, you will be prompted to enter a question:

  ```text
  Do you have a question for me?
  ```
  
  Type your question and press Enter.
  
- The chatbot will categorize your question and respond with a suitable answer from the defined responses in `data.json`.

## Project Structure

```text
project-directory/
│
├─ data.json                 # Contains chatbot intents, patterns, and responses
├─ chatbot_dnnmodel.tflearn  # Saved model file (generated after training)
├─ chatbot_dnnmodel.tflearn.meta
├─ README.md                 # This file
└─ chatbot.py                # Main script
```

## Customization

- Add more intents, patterns, and responses in `data.json`.
- Adjust neural network structure in `build_model()` function.
- Change the threshold in `categorize()` if needed.

## Troubleshooting

- **Model not loading**: Ensure that `chatbot_dnnmodel.tflearn.index` and related files are present if skipping training.
- **NLTK errors**: Make sure that the `punkt` and `stopwords` data are available. The script attempts to download them if missing.
- **TensorFlow or TFLearn version issues**: Check compatibility between TensorFlow and TFLearn versions.

## License

This project is licensed under the [MIT License](LICENSE).
