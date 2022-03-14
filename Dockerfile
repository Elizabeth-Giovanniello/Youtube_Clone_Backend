FROM python:slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

COPY requirements.txt .

RUN apt-get update
RUN apt-get install -y --no-install-recommends gcc libc-dev python3-dev default-libmysqlclient-dev

RUN python -m pip install pip install -r requirements.txt
RUN pip install uwsgi

WORKDIR /app
ADD . /app

# RUN ["chmod", "+x", "/docker/entrypoints/entrypoint.sh"] 
# ENTRYPOINT ["./docker/entrypoints/docker-entrypoint.sh"]

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser