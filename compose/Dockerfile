FROM python:3.8
ENV DockerHOME=/www

RUN mkdir $DockerHOME

WORKDIR $DockerHOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LANGUAGE=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV LC_CTYPE=UTF-8

RUN apt-get update && \
    apt-get install -y \
    build-essential gcc libffi-dev make cmake python3-dev musl-dev libsodium-dev libpq-dev\
    binutils libproj-dev gdal-bin \
    postgresql python3-psycopg2

RUN mkdir ./source
COPY ./source/ ./source
COPY ./requirements ./requirements
COPY ./compose/docker-entrypoint.sh ./entrypoint.sh
COPY ./compose/worker-entrypoint.sh ./worker-entrypoint.sh

RUN chmod +x ./entrypoint.sh
RUN chmod +x ./worker-entrypoint.sh

RUN pip install -r ./requirements/local.txt
EXPOSE 8000
