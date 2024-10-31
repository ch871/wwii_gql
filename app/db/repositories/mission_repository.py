from app.db.database import session_maker
from app.db.models import Mission, Target, City, Country, TargetType


def get_all_missions():
    with session_maker() as session:
        return session.query(Mission).all()


def get_mission_by_id(id):
    with session_maker() as session:
        return session.get(Mission, id)


def get_mission_between_date(start, end):
    with session_maker() as session:
        return session.query(Mission).filter((Mission.mission_date > start) & (Mission.mission_date < end)).all()


def get_mission_by_country(country):
    with session_maker() as session:
        return (session.query(Mission)
                .join(Target)
                .join(City)
                .join(Country)
                .filter(Country.country_name == country).all())


def get_mission_by_target_industry(industry):
    with session_maker() as session:
        return (session.query(Mission)
                .join(Target)
                .filter(Target.target_industry == industry).all())


def get_mission_by_target_type(target_type):
    with session_maker() as session:
        return (session.query(Mission)
                .join(Target)
                .join(TargetType)
                .filter(TargetType.target_type_name == target_type).all())


def create_mission(
                   mission_id,
                   mission_date,
                   airborne_aircraft,
                   attacking_aircraft,
                   bombing_aircraft,
                   aircraft_returned,
                   aircraft_failed,
                   aircraft_damaged,
                   aircraft_lost):
    with session_maker() as session:
        mission = Mission(
            mission_id=mission_id,
            mission_date=mission_date,
            airborne_aircraft=airborne_aircraft,
            attacking_aircraft=attacking_aircraft,
            bombing_aircraft=bombing_aircraft,
            aircraft_returned=aircraft_returned,
            aircraft_failed=aircraft_failed,
            aircraft_damaged=aircraft_damaged,
            aircraft_lost=aircraft_lost)
        session.add(mission)
        session.commit()
        session.refresh(mission)
        return mission
