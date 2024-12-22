from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship

from app.db.database import Base


class Child(Base):
    __tablename__ = "children"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(Enum("M", "F", name="gender_enum"), nullable=False)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        gender = gender.strip().lower()

        if gender in {"m", "male"}:
            self.gender = "M"
        elif gender in {"f", "female"}:
            self.gender = "F"
        else:
            raise ValueError(f"Invalid gender: {gender}. Allowed values are 'M', 'F', 'Male', 'Female'.")
        
    def __repr__(self):
        return f"<Child(id={self.id}, name={self.name}, age={self.age}, gender={self.gender})>"