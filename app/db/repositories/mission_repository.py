from app.db.database import session_maker
from app.db.models import Mission


def get_all_missions():
    with session_maker() as session:
        return session.query(Mission).all()
