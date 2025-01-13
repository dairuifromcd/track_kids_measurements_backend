from datetime import date

from sqlalchemy import Integer, String, Enum, Date
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Child(Base):
    __tablename__ = "children"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    date_of_birth: Mapped[date] = mapped_column(Date, nullable=False)
    gender: Mapped[str] = mapped_column(
        Enum("M", "F", name="gender_enum"),
        nullable=False
    )

    def __init__(self, name, date_of_birth, gender):
        self.name = name
        self.date_of_birth = date_of_birth
        gender = gender.strip().lower()

        if gender in {"m", "male"}:
            self.gender = "M"
        elif gender in {"f", "female"}:
            self.gender = "F"
        else:
            raise ValueError(
                f"Invalid gender: {gender}. "
                f"Allowed values are 'M', 'F', 'Male', 'Female'."
            )

    def __repr__(self):
        return (
            f"<Child(id={self.id}, "
            f"name={self.name}, "
            f"age={self.age}, "
            f"gender={self.gender})>"
        )
