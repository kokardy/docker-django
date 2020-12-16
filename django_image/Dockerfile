FROM python:slim


COPY ./requirement.txt /tmp/requirement.txt

RUN pip install --upgrade pip \
    && pip install -r /tmp/requirement.txt

WORKDIR /asset/project/pro1
