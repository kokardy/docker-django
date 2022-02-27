import graphene

from ..models import Person, Book
from .person import PersonType, CreatePerson
from .book import BookType


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

    def resolve_goodbye(self, info):
        return f"say Ya. \nself:{self} \ninfo:{info}"


class Mutate(graphene.ObjectType):
    create_person = CreatePerson.Field()
