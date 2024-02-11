from utils.repository import SQLAlchemyRepository
from models.cars import Car


class CarsRepository(SQLAlchemyRepository):
    model = Car
