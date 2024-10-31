from app.db.database import session_maker
from app.db.models import Target


def get_all_targets_missions(root):
    with session_maker() as session:
        return session.get(Target, root.mission_id)


def get_all_targets_target_type(root):
    with session_maker() as session:
        return session.query(Target).filter(Target.target_id == root.target_type_id).all()


def create_target(
        target_id,
        target_industry,
        target_priority,
        target_type_id,
        city_id,
        mission_id):
    with session_maker() as session:
        target = Target(
            target_id=target_id,
            target_industry=target_industry,
            target_priority=target_priority,
            target_type_id=target_type_id,
            city_id=city_id,
            mission_id=mission_id)
        session.add(target)
        session.commit()
        session.refresh(target)
        return target
