# Use an official Python runtime as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the required files to the container
COPY . .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn==20.1.0

# Set the environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Expose port 5000 for Gunicorn to listen on
EXPOSE 5000

# Run the Flask app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]