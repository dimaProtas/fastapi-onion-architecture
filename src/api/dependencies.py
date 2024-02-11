from repositories.tasks import TasksRepository
from repositories.users import UsersRepository
from repositories.cars import CarsRepository
from services.tasks import TasksService
from services.users import UsersService
from services.cars import CarsService


def tasks_service():
    return TasksService(TasksRepository)


def users_service():
    return UsersService(UsersRepository)


def cars_service():
    return CarsService(CarsRepository)
