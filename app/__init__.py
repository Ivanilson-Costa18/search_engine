import nltk
from flask import Flask
from app import routes

nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)


