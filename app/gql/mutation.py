from graphene import ObjectType
from app.gql.mutations.mission_mutation import AddMission


class Mutation(ObjectType):
    add_student = AddMission.Field()
