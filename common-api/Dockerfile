# syntax=docker/dockerfile:1

FROM public.ecr.aws/bitnami/python:latest

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
ENV FLASK_APP=server.py
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
