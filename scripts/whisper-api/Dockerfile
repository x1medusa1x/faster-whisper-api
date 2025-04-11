FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

ARG WHISPER_API_PORT=10301
ENV WHISPER_API_PORT=$WHISPER_API_PORT

EXPOSE $WHISPER_API_PORT

CMD uvicorn main:app --host 0.0.0.0 --port $WHISPER_API_PORT
