from app.db.database import session_maker
from app.db.models import Mission


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
        return session.query(Mission).filter(Mission.targets.city.country.country_name == country).all()


def get_mission_by_target_industry(industry):
    with session_maker() as session:
        return session.query(Mission).filter(Mission.targets.target_industry == industry).all()
