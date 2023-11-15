FROM python:3.10-slim

WORKDIR /app
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip3 install -r requirements.txt
EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Command can be overwritten by providing a different command in the template directly.
ENTRYPOINT ["python", "-m", "streamlit",  "run", "Main.py", "--server.port=8501", "--server.address=0.0.0.0"]