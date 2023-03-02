FROM python:3.8-slim

LABEL maiteiner Raphael Ferreira COelho Santos
LABEL description "Dockerfile para criar a imagem de container do meu primeiro exporter"

WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt

CMD python3 exporter.py