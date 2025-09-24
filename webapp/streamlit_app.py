import streamlit as st
import sys
import os

# Add the parent directory of `app` to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.extractor import extract_text
from app.services.embeddings import generate_embedding
from app.services.analysis import calculate_similarity

def main():
    """Main function to run the Streamlit web app."""
    st.set_page_config(page_title="Resume Match AI", page_icon="🤖")

    st.title("📄 Resume Match AI")
    st.markdown("##### Evaluate how well your resume matches a job posting.")

    st.sidebar.header("Instructions")
    st.sidebar.info(
        "1. Upload your resume in PDF or DOCX format.\n"
        "2. Paste the job description you are applying for.\n"
        "3. Click the 'Analyze' button to see the match score."
    )

    uploaded_resume = st.file_uploader(
        "1. Upload Your Resume",
        type=["pdf", "docx"],
        help="Please upload your resume in PDF or DOCX format."
    )

    job_description = st.text_area(
        "2. Paste the Job Description",
        height=300,
        placeholder="Paste the full job description here..."
    )

    if st.button("Analyze ✨"):
        if uploaded_resume is not None and job_description:
            with st.spinner("Analyzing your documents... This may take a moment."):
                # 1. Extract text from documents
                resume_text = extract_text(uploaded_resume, uploaded_resume.name)

                # 2. Generate embeddings for both texts
                st.info("Step 1: Generating embeddings for resume and job description...")
                resume_embedding = generate_embedding(resume_text)
                jd_embedding = generate_embedding(job_description)

                # 3. Calculate similarity score
                st.info("Step 2: Calculating similarity score...")
                match_score = calculate_similarity(resume_embedding, jd_embedding)

            st.success("Analysis Complete!")
            st.subheader(f"Overall Match Score: {match_score:.2f}%")

            # Display a progress bar for visual representation
            st.progress(int(match_score))

            # Optional: Show a summary
            with st.expander("Show Document Previews"):
                st.subheader("Extracted Resume Text (Preview)")
                st.text_area("Resume Content", resume_text, height=200, disabled=True)

                st.subheader("Job Description Text (Preview)")
                st.text_area("Job Description Content", job_description, height=200, disabled=True)
        else:
            st.warning("Please upload a resume and paste a job description.")

if __name__ == "__main__":
    main()