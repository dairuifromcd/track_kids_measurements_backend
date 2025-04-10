from sqlalchemy.orm import Session
from app.models.child import Child
from app.schemas.child import ChildCreate, ChildUpdate


def create_child(db: Session, child: ChildCreate) -> Child:
    child = Child(**child.model_dump())
    db.add(child)
    db.commit()
    db.refresh(child)

    return child


def get_children(db: Session) -> list[Child]:
    return db.query(Child).all()


def update_child(db: Session, child_id: int, child: ChildUpdate) -> Child:
    db_child = db.query(Child).filter(Child.id == child_id).first()
    if db_child is None:
        raise ValueError(f"Child with id {child_id} not found")

    # Get the update data
    update_data = child.model_dump()

    # Handle gender validation separately
    if 'gender' in update_data:
        gender = update_data['gender'].strip().lower()
        if gender in {"m", "male"}:
            update_data['gender'] = "M"
        elif gender in {"f", "female"}:
            update_data['gender'] = "F"
        else:
            raise ValueError(
                f"Invalid gender: {gender}. "
                f"Allowed values are 'M', 'F', 'Male', 'Female'."
            )

    # Update other fields
    for key, value in update_data.items():
        setattr(db_child, key, value)

    db.commit()
    db.refresh(db_child)
    return db_child


def delete_child(db: Session, child_id: int) -> None:
    child = db.query(Child).filter(Child.id == child_id).first()
    db.delete(child)
    db.commit()
