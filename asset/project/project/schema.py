import graphene
from graphene_django import DjangoObjectType

from app1.models import Person as App1Person

class Person(DjangoObjectType):
    class Meta:
        model = App1Person

class Query(graphene.ObjectType):
    #person = graphene.Field(Person, id=graphene.String())
    persons = graphene.List(Person)

    @graphene.resolve_only_args
    def resolve_persons(self):
        return App1Person.objects.all()


schema = graphene.Schema(query=Query)