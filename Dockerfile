FROM python:3-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install flask

COPY . .

CMD python app.py
