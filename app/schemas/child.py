from pydantic import BaseModel

class ChildBase(BaseModel):
    name: str
    gender: str
    age: int

class ChildCreate(ChildBase):
    pass

class ChildRead(ChildBase):
    id: int

    class Config:
        orm_mode = True