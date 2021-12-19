# official image
FROM python:3.9.5-slim-buster

# working dir
WORKDIR /usr/src/app

# env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# dependencies (system and app dependencies)
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy source code
COPY . .

# entrypoint (run the app)
CMD python manage.py run -h 0.0.0.0
