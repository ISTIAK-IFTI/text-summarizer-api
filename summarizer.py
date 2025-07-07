# summarizer.py

import re
import nltk
import numpy as np
import heapq

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize

# Download NLTK resources (only once)
nltk.download('punkt')
nltk.download('stopwords')


def preprocess_text(text):
    """Clean and preprocess the text."""
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'\[[^]]*\]', '', text)  # Remove references like [1]
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = text.strip()
    return text


def summarize_text(text, num_sentences=3):
    """Summarize the input text by extracting top sentences."""
    text = preprocess_text(text)

    # Split into sentences
    sentences = sent_tokenize(text)
    if len(sentences) <= num_sentences:
        return text  # Not enough sentences to summarize

    # Convert sentences to TF-IDF vectors
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    sentence_vectors = tfidf_vectorizer.fit_transform(sentences)

    # Compute sentence similarity matrix
    similarity_matrix = cosine_similarity(sentence_vectors)

    # Score sentences by similarity
    sentence_scores = similarity_matrix.sum(axis=1)

    # Select top N sentence indices
    top_indices = heapq.nlargest(num_sentences, range(len(sentence_scores)), key=sentence_scores.__getitem__)
    top_indices.sort()  # Keep original order

    # Construct summary
    summary = ' '.join([sentences[i] for i in top_indices])
    return summary