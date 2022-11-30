FROM python:3.10.7-slim

EXPOSE 80

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt /app/

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install -r requirements.txt --no-cache-dir \
    && apt-get -y remove libpq-dev gcc

COPY ulticlipper ulticlipper
COPY backend backend
COPY manage.py manage.py

CMD python manage.py makemigrations \
    && python manage.py migrate \
    && gunicorn ulticlipper.wsgi -b 0.0.0.0:80
