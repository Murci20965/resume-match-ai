import unittest
import numpy as np
import sys
import os

# Add the project root to the Python path to allow imports from `app`
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app.services.analysis import calculate_similarity, find_missing_keywords

class TestAnalysisService(unittest.TestCase):

    def test_calculate_similarity_identical(self):
        """Test that identical vectors yield a score of 100."""
        vec1 = np.array([1, 1, 1])
        vec2 = np.array([1, 1, 1])
        score = calculate_similarity(vec1, vec2)
        self.assertAlmostEqual(score, 100.0, places=2)

    def test_calculate_similarity_orthogonal(self):
        """Test that orthogonal (completely different) vectors yield a score of 0."""
        vec1 = np.array([1, 0, 0])
        vec2 = np.array([0, 1, 0])
        score = calculate_similarity(vec1, vec2)
        self.assertAlmostEqual(score, 0.0, places=2)

    def test_find_missing_keywords(self):
        """Test the missing keyword detection logic."""
        jd_keywords = ["python", "machine learning", "streamlit"]
        resume_text = "I have experience with python and streamlit."
        missing = find_missing_keywords(jd_keywords, resume_text)
        self.assertEqual(missing, ["machine learning"])

    def test_find_missing_keywords_none_missing(self):
        """Test when no keywords are missing."""
        jd_keywords = ["python", "streamlit"]
        resume_text = "I have experience with python and streamlit."
        missing = find_missing_keywords(jd_keywords, resume_text)
        self.assertEqual(missing, [])

if __name__ == '__main__':
    unittest.main()