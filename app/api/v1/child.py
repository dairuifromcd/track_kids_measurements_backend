from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.crud.child import create_child, get_children, delete_child
from app.schemas.child import ChildCreate, ChildRead

router = APIRouter()


@router.post("/", response_model=ChildRead)
def create_new_child(child_in: ChildCreate, db: Session = Depends(get_db)):
    return create_child(db, child_in)


@router.get("/", response_model=list[ChildRead])
def list_children(db: Session = Depends(get_db)):
    return get_children(db)


@router.delete("/{child_id}", response_model=ChildRead)
def remove_child(child_id: int, db: Session = Depends(get_db)):
    return delete_child(db, child_id)
