from models.tasks import TaskHistory
from utils.repository import SQLAlchemyRepository


class TasksHistoryRepository(SQLAlchemyRepository):
    model = TaskHistory
