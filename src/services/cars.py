from schemas.cars import CarSchemaAdd, CarSchema
from utils.repository import AbstractRepository


class CarsService:
    def __init__(self, cars_repo: AbstractRepository):
        self.cars_repo: AbstractRepository = cars_repo()

    async def add_cars(self, car: CarSchemaAdd):
        car_dict = car.model_dump()
        car_save = await self.cars_repo.add_one(car_dict)
        return car_save

    async def get_cars(self):
        cars = await self.cars_repo.find_all()
        return cars

    async def update_car(self, car: CarSchema):
        car_dict = car.model_dump()
        car_save = await self.cars_repo.update_one(car_dict)
        return car_save
