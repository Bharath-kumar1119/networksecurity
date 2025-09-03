FROM python:3.10-slim-bookworm

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies and AWS CLI
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    pip install --upgrade pip && \
    pip install awscli && \
    pip install -r requirements.txt && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Default command
CMD ["python3", "app.py"]
