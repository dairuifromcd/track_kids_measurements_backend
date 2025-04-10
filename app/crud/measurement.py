from sqlalchemy.orm import Session
from app.models.measurement import Measurement
from app.schemas.measurement import MeasurementCreate, MeasurementUpdate
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


def update_measurement(
    db: Session,
    measurement_id: int,
    measurement: MeasurementUpdate
) -> Measurement:
    db_measurement = db.query(Measurement).filter(
        Measurement.id == measurement_id
    ).first()
    if db_measurement is None:
        raise ValueError(f"Measurement with id {measurement_id} not found")
    for key, value in measurement.model_dump().items():
        setattr(db_measurement, key, value)
    db.commit()
    db.refresh(db_measurement)
    return db_measurement


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
