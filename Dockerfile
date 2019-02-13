FROM python:3.6

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app
WORKDIR /app

ADD requirements.txt /app/
RUN pip install -r /app/requirements.txt

ADD src/ /app/
