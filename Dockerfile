FROM python:3.11-slim

# Install system dependencies (ffmpeg is usually required for audio/DSP processing)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy all project files into the container
COPY . .

# Automatically install dependencies if a requirements.txt file exists
RUN if [ -f requirements.txt ]; then \
        pip install --no-cache-dir -r requirements.txt; \
    fi

# Set the default script to execute
# (Change "file_handler.py" to whichever script boots up your backend server)
CMD ["python", "file_handler.py"]
