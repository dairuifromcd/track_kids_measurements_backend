from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Integer, Float, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base

if TYPE_CHECKING:
    from app.models.child import Child


class Measurement(Base):
    __tablename__ = "measurements"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    height: Mapped[float] = mapped_column(Float, nullable=False)
    weight: Mapped[float] = mapped_column(Float, nullable=False)
    measure_date: Mapped[date] = mapped_column(Date, nullable=False)

    # FK to Child
    child_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("children.id"),
        nullable=False
    )

    # Relationship back to Child
    child: Mapped["Child"] = relationship(
        "Child",
        back_populates="measurements"
    )

    def __repr__(self):
        return (
            f"<Measurement(id={self.id}, "
            f"height={self.height}, "
            f"weight={self.weight}, "
            f"measure_date={self.measure_date})>"
        )
