from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from db.db import Base
from schemas.tasks import TaskSchema


class Task(Base):
    __tablename__ = 'task'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    assignee_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    def to_read_model(self) -> TaskSchema:
        return TaskSchema(
            id=self.id,
            title=self.title,
            author_id=self.author_id,
            assignee_id=self.assignee_id
        )
