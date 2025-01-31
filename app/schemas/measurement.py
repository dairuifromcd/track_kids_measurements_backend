from pydantic import BaseModel
from datetime import date


class MeasurementBase(BaseModel):
    height: float
    weight: float
    measurement_date: date


class MeasurementCreate(MeasurementBase):
    pass


class MeasurementRead(MeasurementBase):
    id: int

    class Config:
        orm_mode = True
