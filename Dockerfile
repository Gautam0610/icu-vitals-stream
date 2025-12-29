FROM python:3.9-slim-buster

WORKDIR /app

COPY src/vitals_generator.py .

CMD ["python", "vitals_generator.py"]