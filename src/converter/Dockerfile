FROM python:3.10-bullseye

# Install system dependencies and upgrade pip
RUN apt-get update \
  && apt-get install -y --no-install-recommends --no-install-suggests \
  build-essential ffmpeg gcc python3-dev \
  && pip install --no-cache-dir --upgrade pip wheel setuptools

# Set working directory
WORKDIR /app

# Copy requirements file
COPY ./requirements.txt /app

# Install Python dependencies
RUN pip install --no-cache-dir --requirement /app/requirements.txt

# Copy the rest of the application code
COPY . /app

# Define the command to run
CMD ["python3", "consumer.py"]