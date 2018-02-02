FROM python:3.6
ENV PYTHONUNBUFFERED 1
WORKDIR /djdocker
ADD requirements.txt /djdocker/
RUN pip install -r requirements.txt
ADD . /djdocker/
