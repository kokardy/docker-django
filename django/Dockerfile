from kokardy/django

ENV $PROJECT_NAME project
ENV $APP_NAME app1

RUN cd /asset \
    && django-admin startproject $PROJECT_NAME \
    && cd $PROJECT_NAME \

RUN ./manage.py startapp $APP_NAME

WORKDIR /asset/$PROJECT_NAME

CMD ["./manage.py", "runserver", "0.0.0.0:8000"]
