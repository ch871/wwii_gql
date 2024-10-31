from app.db.database import session_maker
from app.db.models import Target


def get_all_targets_missions(root):
    with session_maker() as session:
        return session.query(Target).filter(Target.mission_id == root.id).all()
