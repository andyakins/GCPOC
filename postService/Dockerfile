FROM python:3.4.6-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /gcpoc
WORKDIR /gcpoc
ADD . /gcpoc/

RUN pip install -r requirements.txt

EXPOSE 8081
CMD ["python3","app/postService.py"]
