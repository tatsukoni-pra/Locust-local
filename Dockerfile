FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y \
  build-essential && \
  pip install --upgrade pip \
  locust && \
  echo `python --version`

WORKDIR /app/src
