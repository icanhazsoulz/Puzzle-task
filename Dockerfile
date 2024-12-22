FROM python:latest

WORKDIR /app

COPY main.py source.txt ./

CMD ["python", "main.py"]