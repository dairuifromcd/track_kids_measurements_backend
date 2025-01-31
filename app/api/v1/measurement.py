from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.crud.measurement import (
    create_measurement,
    get_measurements,
    delete_measurements
)
from app.schemas.measurement import MeasurementCreate, MeasurementRead
from datetime import date

router = APIRouter()


@router.post("/", response_model=MeasurementRead)
def create_new_measurement(
    measurement_in: MeasurementCreate,
    db: Session = Depends(get_db)
):
    return create_measurement(db, measurement_in)


@router.get("/{child_id}", response_model=list[MeasurementRead])
def list_measurements(
    child_id: int,
    start_date: date,
    end_date: date | None = None,
    db: Session = Depends(get_db)
):
    if end_date is None:
        end_date = start_date

    return get_measurements(db, child_id, start_date, end_date)


@router.delete("/{child_id}", response_model=MeasurementRead)
def remove_measurements(
    child_id: int,
    start_date: date,
    end_date: date | None = None,
    db: Session = Depends(get_db)
):
    if end_date is None:
        end_date = start_date

    return delete_measurements(db, child_id, start_date, end_date)
