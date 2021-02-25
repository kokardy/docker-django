FROM python:slim

COPY ./requirement.txt /tmp/requirement.txt

RUN pip install --upgrade pip \
    && pip install -r /tmp/requirement.txt \
    && mkdir -p /asset && cd /asset \

CMD ["./manage.py", "runserver", "0.0.0.0:8000"]


