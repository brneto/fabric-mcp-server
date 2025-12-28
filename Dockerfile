FROM python:3.11-slim

# Install git
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy dependency definition
COPY pyproject.toml .

# Install dependencies using uv
# --system installs into the system python environment, avoiding the need for a venv in the container
RUN uv pip install --system -r pyproject.toml

# Copy server code
COPY server.py helpers.py ./

# Create data directory
RUN mkdir -p /app/data

# Run the server
CMD ["python", "server.py"]