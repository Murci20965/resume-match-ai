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