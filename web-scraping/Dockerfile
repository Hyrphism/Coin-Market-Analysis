FROM       python:3.8-slim-buster

WORKDIR    /code

# Install dependencies:
COPY       requirements.txt ./
RUN        pip install -r requirements.txt

COPY       main/ .

CMD        ["python3", "./main.py"]
