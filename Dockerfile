# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# Use --no-cache-dir to keep the image size small
RUN pip install --no-cache-dir -r requirements.txt

# Download the spaCy model during the build process
RUN python -m spacy download en_core_web_sm

# Copy the rest of the application code into the container at /app
COPY . .

# Expose the port the app runs on (Hugging Face uses 7860 for Docker)
EXPOSE 7860

# Define the command to run the app
# Use --server.port to match the exposed port and --server.address to listen on all interfaces
CMD ["streamlit", "run", "webapp/streamlit_app.py", "--server.port=7860", "--server.address=0.0.0.0"]