from graphene import Mutation, Field, Int, Date, Float
from app.db.repositories.mission_repository import create_mission, update_mission
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


class UpdateMission(Mutation):
    class Arguments:
        mission_id = Int()
        aircraft_returned = Float()
        aircraft_failed = Float()
        aircraft_damaged = Float()
        aircraft_lost = Float()

    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info, mission_id, aircraft_returned, aircraft_failed, aircraft_damaged, aircraft_lost):
        return UpdateMission(
            mission=update_mission(mission_id, aircraft_returned, aircraft_failed, aircraft_damaged, aircraft_lost))


class DeleteMission(Mutation):
    class Arguments:
        mission_id = Int(required=True)

    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info, mission_id):
        return DeleteMission(student=delete_mission(mission_id))
