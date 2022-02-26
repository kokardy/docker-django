import graphene
from graphene_django import DjangoObjectType

from app1.schema import Query as App1Query
from app1.schema import Mutate as App1Mutate


class Query(
    App1Query,
    graphene.ObjectType,
):
    pass


class Mutate(
    App1Mutate,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutate)
