import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.extractor import extract_text
from app.services.embeddings import generate_embedding
from app.services.analysis import calculate_similarity, extract_keywords, find_missing_keywords
from app.services.suggestions import generate_suggestions

def main():
    """Main function to run the Streamlit web app."""
    st.set_page_config(page_title="Resume Match AI", page_icon="🤖", layout="wide")

    st.title("📄 Resume Match AI")
    st.markdown("##### Get AI-powered feedback on how well your resume matches a job posting.")

    st.sidebar.header("How to Use")
    st.sidebar.info(
        "1. Upload your resume (PDF/DOCX).\n"
        "2. Paste the target job description.\n"
        "3. Click 'Analyze' for your results."
    )

    col1, col2 = st.columns(2)

    with col1:
        uploaded_resume = st.file_uploader(
            "1. Upload Your Resume",
            type=["pdf", "docx"],
            help="Please upload your resume in PDF or DOCX format."
        )
    with col2:
        job_description = st.text_area(
            "2. Paste the Job Description",
            height=320,
            placeholder="Paste the full job description here..."
        )

    if st.button("Analyze ✨", use_container_width=True):
        if uploaded_resume is not None and job_description:
            with st.spinner("Your personalized analysis is being generated..."):
                resume_text = extract_text(uploaded_resume, uploaded_resume.name)

                # --- Main Analysis ---
                resume_embedding = generate_embedding(resume_text)
                jd_embedding = generate_embedding(job_description)
                match_score = calculate_similarity(resume_embedding, jd_embedding)
                jd_keywords = extract_keywords(job_description)
                missing_keywords = find_missing_keywords(jd_keywords, resume_text)
                suggestions = generate_suggestions(resume_text)

            # --- Display Results ---
            st.header("Analysis Report", divider="rainbow")

            # --- Score Section ---
            st.subheader("Semantic Match Score")
            st.progress(int(match_score), text=f"{match_score:.2f}%")
            st.info(f"This score reflects the semantic similarity between your resume and the job description. A higher score means better alignment.", icon="💡")

            # --- Keywords Section ---
            st.subheader("Keyword Analysis")
            if not missing_keywords:
                st.success("Excellent! Your resume appears to contain all the key skills from the job description.")
            else:
                st.warning(f"Your resume is missing **{len(missing_keywords)}** key skills found in the job description.", icon="⚠️")

                # Display missing keywords in columns for better readability
                num_columns = 3
                cols = st.columns(num_columns)
                for i, keyword in enumerate(missing_keywords):
                    with cols[i % num_columns]:
                        st.markdown(f"- `{keyword}`")

            # --- Suggestions Section ---
            if suggestions:
                st.subheader("Actionable Suggestions")
                for suggestion in suggestions:
                    st.markdown(suggestion)

        else:
            st.warning("Please upload a resume and paste a job description.")

if __name__ == "__main__":
    main()