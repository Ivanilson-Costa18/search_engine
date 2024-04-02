from app import app
import nltk

nltk.download()

if __name__ == '__main__':
    app.run(debug=True)