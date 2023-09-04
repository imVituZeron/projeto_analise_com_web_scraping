FROM python:3.9.16

COPY . /app
WORKDIR /app
RUN apt-get update && apt-get install python3-pip -y && pip install -r requirements.txt
CMD python3 main.py
