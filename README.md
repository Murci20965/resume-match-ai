---
title: Resume Match AI
emoji: 🤖📄
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
---

# Resume Match AI 🤖💼

Resume Match AI is an automated tool to help job seekers evaluate how well their resume matches a job posting. The app produces a match score, highlights missing keywords/skills, and suggests actionable edits to improve the resume's alignment with an Applicant Tracking System (ATS).

This project is being built to demonstrate end-to-end AI engineering capabilities, from data ingestion and NLP modeling to API deployment and frontend development.# 🤖 Resume Match AI

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?logo=streamlit)](https://streamlit.io/)
[![spaCy](https://img.shields.io/badge/spaCy-NLP-blue?logo=spacy)](https://spacy.io/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An **end-to-end NLP application** that scores resumes against job descriptions, highlights missing keywords, and provides actionable suggestions for improvement.  
Built with **Sentence-BERT** for semantic analysis, served via an interactive **Streamlit** UI, and fully **Dockerized** for deployment.

**[🚀 Live Demo Link Here]** ---

## 📌 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Tech-Stack](#-tech-stack)
- [Project-Architecture](#-project-architecture)
- [Setup-and-Installation](#-setup-and-installation)
- [Usage](#-usage)
- [Testing](#-testing)
- [License](#-license)

---

## 📖 Overview
This project provides job seekers with an automated tool to evaluate how well their resume matches a job posting. By leveraging **Sentence-BERT embeddings** for semantic understanding and **spaCy** for NLP-powered keyword extraction, the application goes beyond simple word counting to provide meaningful, actionable feedback.

The system is designed with a clean separation of concerns, isolating the core AI services from the user interface, making it maintainable and scalable.

---

## ✨ Features
✅ **Semantic Match Scoring** – Uses Sentence-BERT and cosine similarity to calculate a score based on meaning, not just keywords.  
✅ **Intelligent Keyword Analysis** – Employs spaCy to extract key skills and noun chunks from job descriptions.  
✅ **Missing Skill Highlighting** – Clearly identifies and lists important keywords found in the job description but missing from the resume.  
✅ **Actionable Suggestions** – Provides heuristic-based tips to improve the resume, such as adding quantifiable metrics and stronger action verbs.  
✅ **Interactive UI** – A clean and simple Streamlit interface for file uploads and text input.  
✅ **Dockerized** – Fully containerized for easy, consistent deployment anywhere.

---

## 🛠 Tech Stack
-   **Language**: Python 3.10+
-   **NLP Models**: `sentence-transformers` (Sentence-BERT), `spaCy`
-   **Web UI**: `Streamlit`
-   **Vector Ops**: `scikit-learn`, `numpy`
-   **Containerization**: `Docker`
-   **Testing**: `unittest` (Python Standard Library)
-   **CI/CD**: `GitHub Actions`

---

## 🏛️ Project Architecture
The project follows a modular structure to ensure clean separation between the UI and the backend AI services.
```
resume_match_ai/
│
├── app/
│   ├── services/
│   │   ├── analysis.py       # Similarity, keyword extraction
│   │   ├── embeddings.py     # Sentence-BERT model wrapper
│   │   ├── extractor.py      # PDF/DOCX text extraction
│   │   └── suggestions.py    # Heuristic suggestions engine
│   └── ...
│
├── tests/
│   └── unit/
│       └── test_analysis.py  # Unit tests for core logic
│
├── webapp/
│   └── streamlit_app.py      # Streamlit user interface
│
├── .github/
│   └── workflows/
│       └── ci.yml            # GitHub Actions CI workflow
│
├── .dockerignore
├── .gitignore
├── Dockerfile                # Recipe for building the application container
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Murci20965/resume-match-ai.git](https://github.com/Murci20965/resume-match-ai.git)
    cd resume-match-ai
    ```

2.  **Create and activate a virtual environment:**
    ```cmd
    python -m venv .venv
    .venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Download the spaCy model:**
    ```bash
    python -m spacy download en_core_web_sm
    ```

---

## 🚀 Usage

### Running the Application Locally
To run the Streamlit web application directly:
```bash
python -m streamlit run webapp/streamlit_app.py
```

### Running with Docker
Ensure Docker Desktop is installed and running.

1.  **Build the Docker image:**
    ```bash
    docker build -t resume-match-ai .
    ```

2.  **Run the container:**
    ```bash
    docker run --rm -p 7860:7860 --name resume-app resume-match-ai
    ```
    Access the application in your browser at `http://localhost:7860`.

---

## ✅ Testing
To run the automated unit tests and ensure the application's core logic is working correctly, use the following command:
```bash
python -m unittest discover tests
```
---

## 📜 License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

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
-   Python 3.11 or higher
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