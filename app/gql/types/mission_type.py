from graphene import ObjectType, Int, List, Date, Float, Field
from app.db.repositories.target_repository import get_all_targets_missions


class MissionType(ObjectType):
    mission_id = Int()
    mission_date = Date()
    airborne_aircraft = Float()
    attacking_aircraft = Float()
    bombing_aircraft = Float()
    aircraft_returned = Float()
    aircraft_failed = Float()
    aircraft_damaged = Float()
    aircraft_lost = Float()

    targets = Field("app.gql.types.target_type.TargetType")

    @staticmethod
    def resolve_targets(root, info):
        return get_all_targets_missions(root)
