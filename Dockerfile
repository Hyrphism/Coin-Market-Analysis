FROM       python:3.8-slim-buster

RUN        mkdir /Project
WORKDIR    /Project

# Install dependencies:
COPY       requirements.txt ./
RUN        pip install -r requirements.txt

COPY       . .

CMD        ["python3", "./main.py"]
