from flask import Flask

app = Flask(__name__)

import nltk
nltk.download('punkt')

from app import routes

