# Use official Python slim image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of application code
COPY . .

# Expose port 5000 (Flask default)
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]