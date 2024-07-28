import collections.abc  # Import collections.abc instead of just collections
import sys
import yaml

# Monkey patch to address the AttributeError for collections.Hashable
if sys.version_info >= (3, 10):
    collections.Hashable = collections.abc.Hashable

from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import nltk

# Download necessary NLTK data
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

chatbot = ChatBot('ChatBot')
trainer = ChatterBotCorpusTrainer(chatbot)

# Function to read corpus with yaml.safe_load
def read_corpus(file_path):
    with open(file_path, 'r') as stream:
        return yaml.safe_load(stream)

# Train the chatbot
trainer.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))

if __name__ == "__main__":
    app.run()
