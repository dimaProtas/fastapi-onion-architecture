from schemas.cars import CarSchemaAdd, CarSchema
from utils.unitofwork import IUnitOfWork


class CarsService:

    async def add_cars(self, car: CarSchemaAdd, uow: IUnitOfWork):
        car_dict = car.model_dump()
        async with uow:
            car_save = await uow.cars.add_one(car_dict)
            await uow.commit()
            return car_save

    async def get_cars(self, uow: IUnitOfWork):
        async with uow:
            cars = await uow.cars.find_all()
            return cars

    async def update_car(self, id: int, car: CarSchema, uow: IUnitOfWork):
        car_dict = car.model_dump()
        async with uow:
            car_save = await uow.cars.update_one(id, car_dict)
            await uow.commit()
            return car_save
