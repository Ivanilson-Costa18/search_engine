from flask import Flask

app = Flask(__name__)

import nltk
nltk.download('punkt')
nltk.download('stopwords')

from app import routes

