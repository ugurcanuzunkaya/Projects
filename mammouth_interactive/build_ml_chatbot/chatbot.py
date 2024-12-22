import json
import os
import random
import numpy
import nltk
from nltk.stem.lancaster import LancasterStemmer
import tflearn
from nltk.data import find


# Check if nltk data is available before downloading
def ensure_nltk_data():
    # Check for 'punkt'
    try:
        find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')
    
    # Check for 'stopwords'
    try:
        find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords')

    # Check for 'punkt_tab'
    try:
        find('corpora/punkt_tab')
    except LookupError:
        nltk.download('punkt_tab')

# Ensure NLTK data is available
ensure_nltk_data()

# Set up paths
script_dir = os.path.dirname(os.path.realpath(__file__))
current_dir = os.getcwd()

if script_dir != current_dir:
    print(f"Changing working directory from {current_dir} to {script_dir}")
    os.chdir(script_dir)

model_file = "chatbot_dnnmodel.tflearn"
data_file = "data.json"

# Load Data
with open(data_file, "r") as json_data:
    data = json.load(json_data)
print(f"Data: {data}")

stemmer = LancasterStemmer()

def preprocess_data(data):
    words = []
    documents = []
    classes = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            # Tokenize
            pattern_words = nltk.word_tokenize(pattern)
            words.extend(pattern_words)
            documents.append((pattern_words, intent["tag"]))

            if intent["tag"] not in classes:
                classes.append(intent["tag"])

    # Stem and lowercase
    words_lowercase = [stemmer.stem(word.lower()) for word in words]
    words = sorted(list(set(words_lowercase)))

    return words, documents, classes

def create_training_data(words, documents, classes):
    empty_output = [0] * len(classes)
    training_data = []

    for document in documents:
        bag_of_words = []
        pattern_words = document[0]
        pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]

        # Create bag of words array
        for word in words:
            bag_of_words.append(1 if word in pattern_words else 0)

        # Create output row
        output_row = list(empty_output)
        output_row[classes.index(document[1])] = 1
        training_data.append([bag_of_words, output_row])

    # Shuffle and convert to numpy
    random.shuffle(training_data)
    training_data = numpy.array(training_data)

    train_X = list(training_data[:, 0])
    train_y = list(training_data[:, 1])

    return train_X, train_y

def build_model(input_size, output_size):
    neural_network = tflearn.input_data(shape=[None, input_size])
    neural_network = tflearn.fully_connected(neural_network, 8)
    neural_network = tflearn.fully_connected(neural_network, 8)
    neural_network = tflearn.fully_connected(neural_network, output_size, activation='softmax')
    neural_network = tflearn.regression(neural_network)
    model = tflearn.DNN(neural_network)
    return model

def process_question(question, words):
    question_tokenized = nltk.word_tokenize(question)
    question_stemmed = [stemmer.stem(word.lower()) for word in question_tokenized]
    bag = [0] * len(words)

    for stem in question_stemmed:
        for index, w in enumerate(words):
            if w == stem:
                bag[index] = 1

    return numpy.array(bag)

def categorize(prediction, classes):
    prediction_top = [[index, result] for index, result in enumerate(prediction) if result > 0.5]
    prediction_top.sort(key=lambda x: x[1], reverse=True)

    result = [
        (classes[prediction_value[0]], prediction_value[1])
        for prediction_value in prediction_top
    ]

    return result

def chatbot_response(question, model, words, classes, data):
    prediction = model.predict([process_question(question, words)])[0]
    category = categorize(prediction, classes)
    if not category:
        return "I'm not sure about that."
    for intent in data["intents"]:
        if intent["tag"] == category[0][0]:
            return random.choice(intent["responses"])
    return "I don't have a response for that."

# Main logic
if os.path.exists(f"{model_file}.index"):
    # Model exists, just load and skip training
    print("Model found. Loading the model...")
    # We still need to preprocess once to get the words/classes structure
    words, documents, classes = preprocess_data(data)
    model = build_model(len(words), len(classes))
    model.load(model_file)
else:
    # Model does not exist: Preprocess data, train and then save the model
    words, documents, classes = preprocess_data(data)
    train_X, train_y = create_training_data(words, documents, classes)

    print(f"Training on {len(train_X)} samples...")
    model = build_model(len(train_X[0]), len(train_y[0]))
    model.fit(train_X, train_y, n_epoch=2000, batch_size=8, show_metric=True)
    model.save(model_file)
    print("Model trained and saved.")

# Example of using the chatbot
question = "Do you sell any coding course?"
print("User:", question)
print("Bot:", chatbot_response(question, model, words, classes, data))

# Interactive prompt
user_input = input("Do you have a question for me? ")
print(chatbot_response(user_input, model, words, classes, data))
