from sqlalchemy.orm import Session
from app.models.child import Child
from app.schemas.child import ChildCreate, ChildRead

def create_child(db: Session, child: ChildCreate) -> Child:
    child = Child(**child.model_dump())
    db.add(child)
    db.commit()
    db.refresh(child)

    return child

def get_children(db: Session):
    return db.query(Child).all()