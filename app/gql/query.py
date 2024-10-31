from graphene import ObjectType, List, Field, Int, Date, String
from app.db.repositories.mission_repository import get_all_missions
from app.gql.tipes.mossion_type import MissionType

missions = get_all_missions()


class Query(ObjectType):
    mission_by_country = List(MissionType, country=String())
    mission_between_date = List(MissionType, start=Date(), end=Date())
    mission_by_id = Field(MissionType, mission_id=Int())
    mission = List(MissionType)

    @staticmethod
    def resolve_mission(root, info):
        return get_all_missions()

    @staticmethod
    def resolve_mission_by_id(root, info, mission_id):
        return next((m for m in missions if m["mission_id"] == mission_id), None)

    @staticmethod
    def resolve_mission_between_date(root, info, start, end):
        return list(m for m in missions if (m["mission_date"] > start & m["mission_date"] < end))

    @staticmethod
    def resolve_mission_by_country(root, info, country):
        return list
