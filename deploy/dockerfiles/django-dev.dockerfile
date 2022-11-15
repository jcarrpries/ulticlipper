FROM python:3.10.7-slim

EXPOSE 80

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt

CMD python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py loaddata backend/fixtures/seed-events.json \
    # && python manage.py collectstatic --no-input \
    && python manage.py runserver 0.0.0.0:80
    # && gunicorn ulticlipper.wsgi -b 0.0.0.0:80
