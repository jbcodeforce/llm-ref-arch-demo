FROM python:3.10
EXPOSE 8501
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN  pip3 install --upgrade pip && pip3 install -r requirements.txt
COPY . .

# Command overriden by docker-compose
ENTRYPOINT ["python", "-m", "streamlit",  "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]