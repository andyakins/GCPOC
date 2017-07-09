FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /gcpoc
WORKDIR /gcpoc
ADD . /gcpoc/

RUN pip install -r requirements.txt

EXPOSE 8080
CMD ["python3","app/getService.py"]
