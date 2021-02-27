import graphene
from graphene_django import DjangoObjectType

from .models import Person, Book

class PersonType(DjangoObjectType):
    class Meta:
        model = Person
class BookType(DjangoObjectType):
    class Meta:
        model = Book

class Query(graphene.ObjectType):
    #person = graphene.Field(PersonType, id=graphene.String())
    persons = graphene.List(PersonType)
    books = graphene.List(BookType)


    @graphene.resolve_only_args
    def resolve_persons(self):
        return Person.objects.all()
    
    @graphene.resolve_only_args
    def resolve_books(self):
        return Book.objects.all()
    


schema = graphene.Schema(query=Query)