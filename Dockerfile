FROM python:3.8

ARG URL_CLUSTER
ARG DB_USERNAME
ARG DB_PASSWORD
ARG DATABASE

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 80

WORKDIR /app

COPY ./app /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
