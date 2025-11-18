# Dockerfile for `flask-devops-demo`.
# Builds a minimal Python 3.12 image, installs dependencies, creates a
# non-root user, copies the application, and runs it under Gunicorn.

FROM python:3.12-slim

WORKDIR /app

# non-root user
RUN groupadd -r flaskuser && useradd -r -g flaskuser flaskuser

# Copy requirements and install dependencies as root
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code and change ownership
COPY --chown=flaskuser:flaskuser . .

# Switch to non-root user
USER flaskuser

# Expose port
EXPOSE 8000

# Health check using Python (no curl)
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"

# Use Gunicorn production server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--access-logfile", "-", "app:app"]