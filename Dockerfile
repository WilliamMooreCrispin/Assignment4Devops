FROM python:3-slim
COPY . /app
WORKDIR /app
CMD python app.py