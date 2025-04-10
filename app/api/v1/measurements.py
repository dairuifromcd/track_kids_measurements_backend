from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from datetime import date
from typing import Sequence
import logging

from app.api.deps import get_db
from app.crud.measurement import (
    create_measurement,
    get_measurements,
    update_measurement,
    delete_measurements
)
from app.schemas.measurement import (
    MeasurementCreate,
    MeasurementRead,
    MeasurementUpdate
)

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", response_model=MeasurementRead)
async def create_measurement_endpoint(
    request: Request,
    measurement: MeasurementCreate,
    db: Session = Depends(get_db)
) -> MeasurementRead:
    logger.debug(f"Request headers: {dict(request.headers)}")
    raw_body = await request.body()
    logger.debug(f"Raw request body: {raw_body.decode()}")
    logger.debug(f"Parsed request body: {measurement.model_dump()}")
    return create_measurement(db, measurement)


@router.get("/")
def get_measurements_endpoint(
    request: Request,
    child_id: int,
    start_date: date,
    end_date: date,
    db: Session = Depends(get_db)
) -> Sequence[MeasurementRead]:
    logger.debug(f"Request headers: {dict(request.headers)}")
    logger.debug(
        f"Query params: child_id={child_id}, "
        f"start_date={start_date}, end_date={end_date}"
    )
    measurements = get_measurements(db, child_id, start_date, end_date)
    return [MeasurementRead.from_orm(m) for m in measurements]


@router.put("/{measurement_id}", response_model=MeasurementRead)
def update_measurement_endpoint(
    request: Request,
    measurement_id: int,
    measurement: MeasurementUpdate,
    db: Session = Depends(get_db)
) -> MeasurementRead:
    logger.debug(f"Request headers: {dict(request.headers)}")
    logger.debug(f"Request body: {measurement.model_dump()}")
    logger.debug(f"Measurement ID: {measurement_id}")
    updated_measurement = update_measurement(db, measurement_id, measurement)
    if not updated_measurement:
        raise HTTPException(status_code=404, detail="Measurement not found")
    return updated_measurement


@router.delete("/")
def delete_measurements_endpoint(
    request: Request,
    child_id: int,
    start_date: date,
    end_date: date,
    db: Session = Depends(get_db)
) -> None:
    logger.debug(f"Request headers: {dict(request.headers)}")
    logger.debug(
        f"Query params: child_id={child_id}, "
        f"start_date={start_date}, end_date={end_date}"
    )
    delete_measurements(db, child_id, start_date, end_date)
