from sentence_transformers import SentenceTransformer
import numpy as np

# Load the model. This is done once when the module is imported.
# The first time this runs, it will download the model from the internet.
# 'all-MiniLM-L6-v2' is a fast and effective model for semantic similarity.
print("Loading Sentence-BERT model...")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("Model loaded successfully.")

def generate_embedding(text: str) -> np.ndarray:
    """
    Generates a numerical embedding for a given text using Sentence-BERT.

    Args:
        text: The input string to embed.

    Returns:
        A numpy array representing the text embedding.
    """
    if not text or not isinstance(text, str):
        # Return a zero vector for empty or invalid input
        return np.zeros(model.get_sentence_embedding_dimension())

    embedding = model.encode(text, convert_to_numpy=True)
    return embedding