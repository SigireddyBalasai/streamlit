# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Streamlit
RUN pip install --no-cache-dir streamlit

# Expose port 80
EXPOSE 80

# Define environment variable
ENV STREAMLIT_PORT=80

# Run streamlit app when the container launches
CMD ["streamlit", "run", "--server.port", "80", "app.py"]
