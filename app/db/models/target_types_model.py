from sqlalchemy import Column, Integer, Date, Float, String
from sqlalchemy.orm import relationship
from app.db.models import Base


class TargetType(Base):
    __tablename__ = "targettypes"
    target_type_id = Column(Integer, primary_key=True, autoincrement=True)
    target_type_name = Column(String)

    targets = relationship("Target", back_populates="target_type", lazy="immediate")
