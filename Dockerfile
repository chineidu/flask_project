# official image
FROM python:3.9.5-slim-buster

# working dir
WORKDIR /usr/src/app

# env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
    && apt-get -y install netcat gcc postgresql \
    && apt-get clean

# dependencies (system and app dependencies)
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy source code
COPY . .

# add entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod a+x /usr/src/app/entrypoint.sh
