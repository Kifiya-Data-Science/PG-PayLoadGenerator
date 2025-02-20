# Use the official Python image as the base
FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy the project files
COPY . /app/

# Install system dependencies
RUN apt-get update && apt-get install -y netcat-openbsd && apt-get clean

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the Django port
EXPOSE 8000

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "KifiyaDataStub.wsgi:application"]
