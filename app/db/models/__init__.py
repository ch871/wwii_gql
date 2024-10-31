from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .cities_model import City
from .missions_model import Mission
from .targets_model import Target
from .target_types_model import TargetType
from .countries_model import Country
