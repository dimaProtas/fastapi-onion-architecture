from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from db.db import Base
from schemas.cars import CarSchema


class Car(Base):
    __tablename__ = 'car'

    id: Mapped[int] = mapped_column(primary_key=True)
    brand: Mapped[str]
    model: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))

    def to_read_model(self) -> CarSchema:
        return CarSchema(
            id=self.id,
            brand=self.brand,
            model=self.model,
            user_id=self.user_id
        )
