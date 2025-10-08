title: Resume_match_AI
emoji: ⚡
colorFrom: red
colorTo: green
sdk: docker
pinned: false
license: mit
short_description: AI Resume Match

# Resume Match AI 🤖💼

Resume Match AI is an automated tool to help job seekers evaluate how well their resume matches a job posting. The app produces a match score, highlights missing keywords/skills, and suggests actionable edits to improve the resume's alignment with an Applicant Tracking System (ATS).

This project is being built to demonstrate end-to-end AI engineering capabilities, from data ingestion and NLP modeling to API deployment and frontend development.

![Demo Screenshot (coming soon)]()

## ✨ Features (Phase 1)
-   **Resume Parsing**: Extracts text from PDF and DOCX resume files.
-   **Job Description Analysis**: Processes text from pasted job descriptions.
-   **Semantic Match Scoring**: Uses Sentence-BERT embeddings to calculate a semantic similarity score.
-   **Keyword Analysis**: Identifies critical keywords in the job description that are missing from the resume.
-   **Actionable Suggestions**: Provides heuristic-based recommendations to improve the resume.

## 🚀 Live Demo
[Link to deployed Streamlit/Hugging Face app will be here]

## 🛠️ Tech Stack
-   **Language**: Python 3.10+
-   **Models & NLP**: `sentence-transformers`, `spaCy`, `scikit-learn`
-   **API**: `FastAPI`
-   **Prototype UI**: `Streamlit`
-   **Deployment**: Hugging Face Spaces / Streamlit Cloud

## 📦 Getting Started

### Prerequisites
-   Python 3.10 or higher
-   Git

### Installation
1.  Clone the repository:
    ```bash
    git clone [https://github.com/Murci20965/resume-match-ai.git](https://github.com/Murci20965/resume-match-ai.git)
    cd resume-match-ai
    ```

2.  Create and activate a virtual environment:
    ```cmd
    python -m venv .venv
    .venv\Scripts\activate
    ```

3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application
To run the Streamlit web application:
```bash
streamlit run webapp/streamlit_app.py