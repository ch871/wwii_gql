from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.models import Base


class City(Base):
    __tablename__ = "cities"
    city_id = Column(Integer, primary_key=True, autoincrement=True)
    city_name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

    country_id = Column(Integer, ForeignKey("countries.country_id"))

    country = relationship("Country", back_populates="countries")
    targets = relationship("Target", back_populates="city", lazy="immediate")
