from app.db.database import session_maker
from app.db.models import Target


def get_all_targets_missions(root):
    with session_maker() as session:
        return session.get(Target, root.mission_id)


def get_all_targets_target_type(root):
    with session_maker() as session:
        return session.query(Target).filter(Target.target_id == root.target_type_id).all()
