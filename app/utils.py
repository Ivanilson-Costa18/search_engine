from collections import defaultdict
import re, math
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def preprocess_query(query):
    tokens = word_tokenize(query)
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()
    processed_tokens = [stemmer.stem(token.lower()) for token in tokens if token.isalnum() and token.lower() not in stop_words]
    return processed_tokens

def build_inverted_index(documents):
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