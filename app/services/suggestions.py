import re

# A list of common action verbs found in strong resumes
ACTION_VERBS = [
    'developed', 'managed', 'led', 'created', 'implemented', 'designed',
    'optimized', 'achieved', 'negotiated', 'streamlined', 'analyzed'
]

def generate_suggestions(resume_text: str) -> list[str]:
    """
    Generates actionable suggestions based on a heuristic analysis of the resume text.

    Args:
        resume_text: The full text of the resume.

    Returns:
        A list of suggestion strings.
    """
    suggestions = []
    resume_text_lower = resume_text.lower()

    # Suggestion 1: Check for quantifiable metrics
    if not re.search(r'\d+', resume_text): # Checks if there are any digits
        suggestions.append(
            "📈 **Add Quantifiable Metrics:** Your resume could be stronger by including numbers. For example, instead of 'improved performance,' try 'improved performance by 15%'."
        )

    # Suggestion 2: Check for action verbs
    found_verbs = [verb for verb in ACTION_VERBS if verb in resume_text_lower]
    if len(found_verbs) < 3: # Arbitrary threshold for the suggestion
        suggestions.append(
            "🗣️ **Use Strong Action Verbs:** Start bullet points with impactful action verbs like 'developed,' 'managed,' or 'optimized' to describe your accomplishments."
        )

    # Suggestion 3: Check resume length (a very rough heuristic)
    word_count = len(resume_text.split())
    if word_count > 800:
         suggestions.append(
            "📄 **Conciseness is Key:** Your resume seems a bit long. Aim for a one-page resume for less than 10 years of experience, focusing on the most relevant achievements."
        )

    return suggestions