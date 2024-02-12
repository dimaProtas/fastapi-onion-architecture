from fastapi import APIRouter, Depends
from typing import Annotated
from services.cars import CarsService
from api.dependencies import UOWDep
from schemas.cars import CarSchemaAdd, CarSchema

router = APIRouter(
    prefix='/car',
    tags=['Cars']
)


@router.post('/add_cars')
async def add_cars(car: CarSchemaAdd, uow: UOWDep):
    car_new = await CarsService().add_cars(car, uow)
    return {"car": car_new}


@router.get('/get_cars')
async def get_cars(uow: UOWDep):
    cars = await CarsService().get_cars(uow)
    return {"cars": cars}


@router.put('/update_car/{car_id}')
async def update_car(car_id: int, car: CarSchemaAdd, uow: UOWDep):
    car_update = await CarsService().update_car(car_id, car, uow)
    return {"car": car_update}
