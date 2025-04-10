from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import Sequence
import logging

from app.api.deps import get_db
from app.crud.child import (
    create_child,
    get_children,
    update_child,
    delete_child
)
from app.schemas.child import ChildCreate, ChildRead, ChildUpdate

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", response_model=ChildRead)
def create_child_endpoint(
    request: Request,
    child: ChildCreate,
    db: Session = Depends(get_db)
) -> ChildRead:
    logger.debug(f"Request headers: {dict(request.headers)}")
    logger.debug(f"Request body: {child.model_dump()}")
    return create_child(db, child)


@router.get("/", response_model=Sequence[ChildRead])
def get_children_endpoint(
    request: Request,
    db: Session = Depends(get_db)
) -> Sequence[ChildRead]:
    logger.debug(f"Request headers: {dict(request.headers)}")
    children = get_children(db)
    return [ChildRead.from_orm(c) for c in children]


@router.put("/{child_id}", response_model=ChildRead)
def update_child_endpoint(
    request: Request,
    child_id: int,
    child: ChildUpdate,
    db: Session = Depends(get_db)
) -> ChildRead:
    logger.debug(f"Request headers: {dict(request.headers)}")
    logger.debug(f"Request body: {child.model_dump()}")
    logger.debug(f"Child ID: {child_id}")
    updated_child = update_child(db, child_id, child)
    if not updated_child:
        raise HTTPException(status_code=404, detail="Child not found")
    return updated_child


@router.delete("/{child_id}")
def delete_child_endpoint(
    request: Request,
    child_id: int,
    db: Session = Depends(get_db)
) -> None:
    logger.debug(f"Request headers: {dict(request.headers)}")
    logger.debug(f"Child ID: {child_id}")
    delete_child(db, child_id)
