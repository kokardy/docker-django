import graphene
from graphene_django import DjangoObjectType

from app1.schema import Query as App1Query


class Query(
        App1Query,
        graphene.ObjectType,
        ):
    pass



schema = graphene.Schema(query=Query)