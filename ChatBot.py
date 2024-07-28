import collections.abc  # Import collections.abc instead of just collections
import sys
import yaml

# Monkey patch to address the AttributeError for collections.Hashable
if sys.version_info >= (3, 10):
    collections.Hashable = collections.abc.Hashable

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer  # Import ChatterBotCorpusTrainer
import nltk

# Download necessary NLTK data
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('stopwords')

# Initialize the chatbot
chatBot = ChatBot('ChatBot')

# Train the chatbot using ChatterBotCorpusTrainer
trainer = ChatterBotCorpusTrainer(chatBot)
trainer.train("chatterbot.corpus.english")

print("Hi, I am ChatBot")
#print(chatBot.get_response("What is AI?"))

while True:
    query = input("You: ")
    response = chatBot.get_response(query)
    print("ChatBot: {}".format(response))
