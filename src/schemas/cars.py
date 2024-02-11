from pydantic import BaseModel


class CarSchema(BaseModel):
    id: int
    brand: str
    model: str
    user_id: int

    class Config:
        from_attributes = True


class CarSchemaAdd(BaseModel):
    brand: str
    model: str
    user_id: int
