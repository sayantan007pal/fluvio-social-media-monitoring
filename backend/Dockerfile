# Dockerfile for backend

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt \
    && pip install tensorflow && pip install torch

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]




