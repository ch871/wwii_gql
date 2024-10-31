from graphene import ObjectType, List, Field, Int, Date, String
from app.db.repositories.mission_repository import get_all_missions, get_mission_by_id, get_mission_between_date, \
    get_mission_by_country, get_mission_by_target_industry
from app.gql.tipes.mossion_type import MissionType


class Query(ObjectType):
    mission_by_target_industry = List(MissionType,industry=String())
    mission_by_country = List(MissionType, country=String())
    mission_between_date = List(MissionType, start=Date(), end=Date())
    mission_by_id = Field(MissionType, mission_id=Int())
    mission = List(MissionType)

    @staticmethod
    def resolve_mission(root, info):
        return get_all_missions()

    @staticmethod
    def resolve_mission_by_id(root, info, mission_id):
        return get_mission_by_id(mission_id)

    @staticmethod
    def resolve_mission_between_date(root, info, start, end):
        return get_mission_between_date(start, end)

    @staticmethod
    def resolve_mission_by_country(root, info, country):
        return get_mission_by_country(country)

    @staticmethod
    def resolve_mission_by_target_industry(root, info, industry):
        return get_mission_by_target_industry(industry)
