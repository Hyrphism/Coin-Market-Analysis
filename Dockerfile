FROM       python:3.8-slim-buster

WORKDIR    /home/hyphersism/Project

# Install dependencies:
COPY       requirements.txt ./
RUN        pip3 install -r requirements.txt

COPY       . .

CMD        ["python3"]
