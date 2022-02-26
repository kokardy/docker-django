import graphene
from graphene import relay
from graphene_django import DjangoObjectType

# from graphene_django.filter import DjangoFilterConnectionField

from .models import Person, Book


class PersonType(DjangoObjectType):
    class Meta:
        interfaces = (relay.Node,)
        model = Person
        filter_fields = ("id", "name", "age")
        interfaces = (graphene.relay.Node,)


class CreatePerson(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        age = graphene.Int(required=True)
        books = graphene.List(graphene.Int)

    person = graphene.Field(PersonType)

    def mutate(root, info, name, age, books):
        person = Person(name=name, age=age)
        person.books = books
        person.save()
        return CreatePerson(person=person)


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


class Mutate(graphene.ObjectType):
    create_person = CreatePerson.Field()
