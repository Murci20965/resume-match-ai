import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(embedding1: np.ndarray, embedding2: np.ndarray) -> float:
    """
    Calculates the cosine similarity between two embedding vectors.

    Args:
        embedding1: The first embedding vector.
        embedding2: The second embedding vector.

    Returns:
        A float representing the similarity score (between 0 and 100).
    """
    # Cosine similarity expects 2D arrays, so we reshape our 1D vectors
    embedding1 = embedding1.reshape(1, -1)
    embedding2 = embedding2.reshape(1, -1)

    # Calculate similarity
    sim_score = cosine_similarity(embedding1, embedding2)[0][0]

    # Convert to a percentage score from 0 to 100
    # We clip to ensure the score is always non-negative
    return max(0, sim_score) * 100

import spacy
import re
from collections import Counter

# Load the spaCy model
# This is loaded once and reused
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading spaCy model...")
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def extract_keywords(text: str) -> list[str]:
    """
    Extracts keywords (noun chunks and proper nouns) from text using spaCy.

    Args:
        text: The text from the job description.

    Returns:
        A list of unique, cleaned keywords.
    """
    doc = nlp(text.lower()) # Process text in lowercase
    keywords = set()

    # We focus on noun chunks as they often represent skills, tools, or concepts
    for chunk in doc.noun_chunks:
        # Clean the chunk by removing stop words, punctuation, and digits
        clean_chunk = ' '.join(
            token.text for token in chunk 
            if not token.is_stop and not token.is_punct and not token.like_num
        )
        if clean_chunk.strip(): # Ensure the chunk is not empty after cleaning
            keywords.add(clean_chunk.strip())

    # We also add important single proper nouns
    for token in doc:
        if token.pos_ == "PROPN" and not token.is_stop and not token.is_punct:
            keywords.add(token.text)

    # For simplicity, we'll return a sorted list of the most common keywords
    # A more advanced version might use TF-IDF or other ranking
    return sorted(list(keywords))


def find_missing_keywords(jd_keywords: list[str], resume_text: str) -> list[str]:
    """
    Compares job description keywords against resume text to find what's missing.

    Args:
        jd_keywords: A list of keywords from the job description.
        resume_text: The full text of the resume.

    Returns:
        A list of keywords that are present in the JD but not in the resume.
    """
    resume_text_lower = resume_text.lower()
    missing = [
        keyword for keyword in jd_keywords 
        if keyword not in resume_text_lower
    ]
    return missing