import graphene
from graphene_django import DjangoObjectType

from app1.models import Person, Book


class PersonType(DjangoObjectType):
    class Meta:
        model = Person
        filter_fields = ("id", "name", "age")


class CreatePerson(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        age = graphene.Int(required=True)
        books = graphene.List(graphene.Int)

    person = graphene.Field(PersonType)

    def mutate(self, info, name, age, books):
        print(f"info:{info}")
        person = Person(name=name, age=age)
        person.books = Book.objects.filter(pk__in=books)
        person.save()
        return CreatePerson(person=person)
