FROM python:3.10.7-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . .

CMD python manage.py test
