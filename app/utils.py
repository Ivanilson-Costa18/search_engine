import re 
import math
from collections import defaultdict
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def preprocess_query(query):
    """
    Preprocesses the input query by tokenizing, removing stopwords, and stemming.

    Args:
        query (str): The input query string.

    Returns:
        list: The list of processed tokens.
    """
    tokens = word_tokenize(query)
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()
    processed_tokens = [stemmer.stem(token.lower()) for token in tokens if token.isalnum() and token.lower() not in stop_words]
    return processed_tokens

def build_inverted_index(documents):
    """
    Build an inverted index from a collection of documents.

    This function takes a list of documents, where each document is represented as
    a dictionary containing 'title' and 'content' fields. It preprocesses each document,
    tokenizes the title and content, computes term frequencies, and constructs an inverted
    index where each term maps to a dictionary of document IDs and their corresponding frequencies.

    Args:
        documents (list): A list of dictionaries representing documents.
            Each dictionary contains 'title' and 'content' fields.

    Returns:
        defaultdict: An inverted index where each term maps to a dictionary of
            document IDs and their corresponding frequencies.
    """
    inverted_index = defaultdict(dict)
    for doc_id, document in enumerate(documents, 1):
        title_tokens = preprocess_query(document['title'])
        content_tokens = preprocess_query(document['content'])
        all_tokens = title_tokens + content_tokens
        term_freq = defaultdict(int)
        for term in all_tokens:
            term_freq[term] += 1
        for term, freq in term_freq.items():
            inverted_index[term][doc_id] = freq
    return inverted_index

def rank_documents(query, inverted_index, documents):
    """
    Rank documents based on a given query using the BM25 ranking algorithm.

    This function ranks the documents in the collection based on the relevance
    to the input query using the BM25 ranking algorithm. It computes scores for
    each document by considering the term frequency, inverse document frequency,
    and document length normalization.

    Args:
        query (str): The input query string.
        inverted_index (defaultdict): An inverted index where each term maps to
            a dictionary of document IDs and their corresponding term frequencies.
        documents (list): A list of dictionaries representing documents.
            Each dictionary contains 'title' and 'content' fields.

    Returns:
        list: A list of tuples containing ranked documents and their corresponding scores.
            Each tuple consists of a document dictionary and its score.
    """
    scores = defaultdict(float)
    N = len(documents)
    avg_doc_length = sum(len(preprocess_query(doc['title']) + preprocess_query(doc['content'])) for doc in documents) / N
    query_terms = preprocess_query(query)
    k1 = 1.5
    b = 0.75
    for term in query_terms:
        if term in inverted_index:
            df = len(inverted_index[term])
            idf = math.log((N - df + 0.5) / (df + 0.5) + 1)
            for doc_id, freq in inverted_index[term].items():
                doc_length = len(preprocess_query(documents[doc_id - 1]['title']) + preprocess_query(documents[doc_id - 1]['content']))
                tf = freq
                score = idf * ((tf * (k1 + 1)) / (tf + k1 * (1 - b + b * (doc_length / avg_doc_length))))
                scores[doc_id] += score
    ranked_documents = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [(documents[doc_id - 1], score) for doc_id, score in ranked_documents if score > 0.5]

def prepare_results(query):
    """
    Prepare search results with highlighted snippets for a given query.

    This function prepares search results for the given query by ranking documents
    based on relevance and formatting the results with highlighted snippets. It
    retrieves the inverted index and documents from the 'app.documents' module,
    ranks documents using the 'rank_documents' function, and formats the results
    with highlighted snippets based on the query terms. The formatted results
    include the document title, snippet of content with query terms highlighted,
    and the document score.

    Args:
        query (str): The input query string.

    Returns:
        dict: A dictionary containing the query, total number of results,
            and a list of formatted search results. Each search result
            includes the title, highlighted content snippet, and score.
    """
    from app.documents import inverted_index, documents
    results = rank_documents(query, inverted_index, documents)
    total_results = len(results)
    formatted_results = []
    for result in results:
        doc = result[0]
        score = result[1]
        title = doc['title']
        content = doc['content']

        snippet_length = 300
        query_terms = preprocess_query(query)
        highlighted_content = content[:snippet_length]
        for term in query_terms:
            highlighted_content = re.sub(r'\b({})\b'.format(re.escape(term)), r'<b>\1</b>', highlighted_content, flags=re.IGNORECASE)
        
        if len(content) > snippet_length:
            highlighted_content += '...'
        
        formatted_result = {
            "title": title,
            "content": highlighted_content,
            "score": score
        }
        formatted_results.append(formatted_result)
    
    response_data = {
        "query": query,
        "total_results": total_results,
        "results": formatted_results
    }
    return response_data
