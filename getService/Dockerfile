FROM python:3.6-alpine
RUN apk update
RUN apk add --no-cache binutils
RUN apk add --no-cache gcc
RUN apk add --no-cache musl-dev
RUN apk add --no-cache mariadb-dev
RUN apk add --no-cache mariadb-client
RUN apk add --no-cache mysql-client

ENV PYTHONUNBUFFERED 1

RUN pip install mysqlclient

CMD ["python3"]
