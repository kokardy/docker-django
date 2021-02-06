FROM python:slim

WORKDIR /asset/project/pro1

COPY ./requirement.txt /tmp/requirement.txt

RUN pip install --upgrade pip \
    && pip install -r /tmp/requirement.txt



