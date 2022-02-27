from graphene_django import DjangoObjectType

# from graphene_django.filter import DjangoFilterConnectionField

from app1.models import Book


class BookType(DjangoObjectType):
    class Meta:
        model = Book
