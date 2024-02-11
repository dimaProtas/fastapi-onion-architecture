from utils.repository import SQLAlchemyRepository
from models.users import User


class UsersRepository(SQLAlchemyRepository):
    model = User