import nltk
from flask import Flask

nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

from app import routes
