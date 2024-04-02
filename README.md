# Search Engine
Welcome to the Search Engine project! This project aims to implement a simple search engine using the BM25 algorithm for efficient retrieval of documents based on user queries.

## Features
- Query Processing: Accepts user queries and processes them for searching.
- Indexing: Indexes documents for quick retrieval based on queries.
- Ranking: Ranks search results using the BM25 algorithm for relevance.
- Output: Presents search results to the user.

## Architecture
The search engine follows a modular architecture:
``` rust
| User Input | -> | Query Processor | -> | Indexing | -> | Ranking | -> | Output |
```
- User Input: Receives user queries.
- Query Processor: Processes user queries for search.
- Indexing: Indexes documents for efficient retrieval.
- Ranking: Ranks search results using the BM25 algorithm.
- Output: Presents search results to the user.

## Retrieval Model
In this project, we have chosen the BM25 algorithm as our retrieval model.

### BM25 Algorithm
BM25, short for "Best Matching 25," is a ranking function used to estimate the relevance of documents to a given search query. It is an extension of the TF-IDF (Term Frequency-Inverse Document Frequency) weighting scheme, incorporating factors such as document length normalization and term saturation.

Key Features of BM25:
- Term Frequency (TF): Measures the frequency of a term in a document. Unlike traditional TF-IDF, BM25 incorporates saturation to prevent excessive weightage for highly frequent terms.
- Inverse Document Frequency (IDF): Measures the importance of a term across the entire document collection. Rare terms are given higher weightage, while common terms are penalized.
- Document Length Normalization: Accounts for variations in document lengths by normalizing the term frequency based on the document length.
- Parameter Tuning: BM25 introduces tunable parameters (k1, b) that allow fine-tuning of the algorithm's behavior to better suit specific datasets and user preferences. 

Advantages of BM25:
- Efficiency: BM25 is computationally efficient, making it suitable for large document collections.
- Scalability: It scales well with the size of the document corpus, maintaining performance even as the dataset grows.
- Flexibility: The tunable parameters allow customization of the algorithm to optimize retrieval performance for different datasets and use cases.
By employing the BM25 algorithm, our search engine can efficiently retrieve relevant documents, providing users with accurate and meaningful search results tailored to their queries.

## Installation
Clone the repository:
```bash
git clone https://github.com/Ivanilson-Costa18/search_engine.git
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Usage
Run the application:
```bash
python3 run.py #development run
uwsgi --http 127.0.0.1:8000 --master -p 4 -w app:app #production run
```
Access the search engine interface via your web browser at http://127.0.0.1:5000.

## License
This project is licensed under the MIT License.

