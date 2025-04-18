from pydantic import BaseModel
from datetime import date


class ChildBase(BaseModel):
    name: str
    date_of_birth: date
    gender: str


class ChildCreate(ChildBase):
    pass


class ChildUpdate(ChildBase):
    pass


class ChildRead(ChildBase):
    id: int

    class Config:
        from_attributes = True
