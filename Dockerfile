FROM python:3.14-slim

ENV PYTHONUNBUFFERED=1 \
    PORT=8080

WORKDIR /app

COPY app.py .

USER 1000

EXPOSE 8080

CMD ["python3", "app.py"]
