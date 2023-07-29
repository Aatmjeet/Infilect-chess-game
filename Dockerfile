# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the entire app directory into the container
COPY . .

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which your Flask app will run (adjust this if needed)
EXPOSE 8000

# Command to run your Flask app
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8000"]