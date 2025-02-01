from pydantic import BaseModel
from datetime import date


class MeasurementBase(BaseModel):
    child_id: int
    height: float
    weight: float
    measure_date: date


class MeasurementCreate(MeasurementBase):
    pass


class MeasurementRead(MeasurementBase):
    id: int

    class Config:
        orm_mode = True
