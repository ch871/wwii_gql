from graphene import Mutation, Field, Int, String
from app.db.repositories.target_repository import create_target
from app.gql.types.target_type import TargetType


class AddTarget(Mutation):
    class Arguments:
        target_id = Int()
        target_industry = String()
        target_priority = String()
        target_type_id = Int()
        city_id = Int()
        mission_id = Int()

    target = Field(TargetType)

    @staticmethod
    def mutate(root,
               info,
               target_id,
               target_industry,
               target_priority,
               target_type_id,
               city_id,
               mission_id
               ):
        return AddTarget(
            mission=create_target(
                target_id,
               target_industry,
               target_priority,
               target_type_id,
               city_id,
               mission_id)
        )
