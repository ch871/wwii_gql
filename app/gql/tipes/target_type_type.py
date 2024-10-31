from graphene import ObjectType, Int, List, String
from app.db.repositories.target_repository import get_all_targets_missions


class TargetTypeType(ObjectType):
    target_type_id = Int()
    target_type_name = String()

    targets = List("app.gql.tipes.target_tipe.TargetType")

    @staticmethod
    def resolve_targets(root, info):
        return get_all_targets_target_type(root)