from graphene import Mutation, Field, Int, Date, Float
from app.db.repositories.mission_repository import create_mission
from app.gql.types.mission_type import MissionType


class AddMission(Mutation):
    class Arguments:
        mission_id = Int()
        mission_date = Date()
        airborne_aircraft = Float()
        attacking_aircraft = Float()
        bombing_aircraft = Float()
        aircraft_returned = Float()
        aircraft_failed = Float()
        aircraft_damaged = Float()
        aircraft_lost = Float()

    mission = Field(MissionType)

    @staticmethod
    def mutate(root,
               info,
               mission_id,
               mission_date,
               airborne_aircraft,
               attacking_aircraft,
               bombing_aircraft,
               aircraft_returned,
               aircraft_failed,
               aircraft_damaged,
               aircraft_lost):
        return AddMission(
            mission=create_mission(
                                   mission_id,
                                   mission_date,
                                   airborne_aircraft,
                                   attacking_aircraft,
                                   bombing_aircraft,
                                   aircraft_returned,
                                   aircraft_failed,
                                   aircraft_damaged,
                                   aircraft_lost)
        )
