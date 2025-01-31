from sqlalchemy.orm import Session
from app.models.measurement import Measurement
from app.schemas.measurement import MeasurementCreate
from datetime import date


def create_measurement(
    db: Session,
    measurement: MeasurementCreate
) -> Measurement:
    measurement = Measurement(**measurement.model_dump())
    db.add(measurement)
    db.commit()
    db.refresh(measurement)

    return measurement


def get_measurements(
    db: Session,
    child_id: int,
    start_date: date,
    end_date: date
) -> list[Measurement]:
    measurements = db.query(Measurement).filter(
        Measurement.child_id == child_id,
        Measurement.measure_date >= start_date,
        Measurement.measure_date <= end_date
    ).all()

    return measurements


def delete_measurements(
    db: Session,
    child_id: int,
    start_date: date,
    end_date: date
) -> None:
    measurements = get_measurements(db, child_id, start_date, end_date)

    for measurement in measurements:
        db.delete(measurement)

    db.commit()
