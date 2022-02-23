import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Person, Book


class PersonType(DjangoObjectType):
    class Meta:
        model = Person
        filter_fields = ("id", "name", "age")
        interfaces = (graphene.relay.Node,)


class BookType(DjangoObjectType):
    class Meta:
        model = Book


class Query(graphene.ObjectType):
    persons = graphene.Field(PersonType, id=graphene.Int())
    books = graphene.List(BookType)

    goodbye = graphene.String()

    @graphene.resolve_only_args
    def resolve_person(self, id):
        return Person.objects.filter(pk=id).first()

    @graphene.resolve_only_args
    def resolve_books(self):
        return Book.objects.all()

    def resolve_goodbye(root, info):
        return "say Ya"
