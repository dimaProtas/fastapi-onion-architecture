from utils.repository import SQLAlchemyRepository
from models.tasks import Task


class TasksRepository(SQLAlchemyRepository):
    model = Task
