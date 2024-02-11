from fastapi import APIRouter, Depends
from typing import Annotated
from services.cars import CarsService
from api.dependencies import cars_service
from schemas.cars import CarSchemaAdd, CarSchema

router = APIRouter(
    prefix='/car',
    tags=['Cars']
)


@router.post('/add_cars')
async def add_cars(car: CarSchemaAdd, cars_service: Annotated[CarsService, Depends(cars_service)]):
    car_new = await cars_service.add_cars(car)
    return car_new


@router.get('/get_cars')
async def get_cars(cars_service: Annotated[CarsService, Depends(cars_service)]):
    cars = await cars_service.get_cars()
    return cars


@router.put('/update_car')
async def update_car(car: CarSchema, cars_service: Annotated[CarsService, Depends(cars_service)]):
    car_update = await cars_service.update_car(car)
    return car_update