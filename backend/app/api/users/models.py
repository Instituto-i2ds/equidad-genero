from typing import List
from sqlalchemy import Column, ForeignKey, String, Integer, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()


def generate_uuid():
    return str(uuid.uuid4())


class AbstractBase(Base):
    __abstract__ = True
    id = Column(String(36), primary_key=True, default=generate_uuid)


class Users(AbstractBase):
    __tablename__ = "Users"

    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    Companies = relationship("Companies", back_populates="user")


class Companies(AbstractBase):
    __tablename__ = "Companies"

    name = Column(String(255), nullable=False)
    user_id = Column(String(36), ForeignKey("Users.id"), nullable=False)
    country_id = Column(String(36), ForeignKey("Countries.id"), nullable=False)
    state_id = Column(String(36), ForeignKey("States.id"), nullable=False)
    sector = Column(String(100), nullable=True)  # New column
    company_size = Column(String(100), nullable=True)  # New column

    user = relationship("Users", back_populates="Companies")
    country = relationship("Countries", back_populates="Companies")
    state = relationship("States", back_populates="Companies")
    employees = relationship("Employees", back_populates="company")


class Employees(AbstractBase):
    __tablename__ = "Employees"

    salary = Column(Numeric(precision=10, scale=2), nullable=False)
    gender = Column(String(10), nullable=False)
    department = Column(String(100), nullable=False)
    position = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    years_at_company = Column(Integer, nullable=False)
    company_id = Column(String(36), ForeignKey("Companies.id"), nullable=False)
    country_id = Column(String(36), ForeignKey("Countries.id"), nullable=False)
    state_id = Column(String(36), ForeignKey("States.id"), nullable=False)

    company = relationship("Companies", back_populates="employees")
    country = relationship("Countries", back_populates="employees")
    state = relationship("States", back_populates="employees")


class Countries(AbstractBase):
    __tablename__ = "Countries"

    name = Column(String(100), nullable=False)
    abbreviation = Column(String(10), nullable=False)

    Companies = relationship("Companies", back_populates="country")
    employees = relationship("Employees", back_populates="country")
    states = relationship("States", back_populates="country")


class States(AbstractBase):
    __tablename__ = "States"

    name = Column(String(100), nullable=False)
    abbreviation = Column(String(10), nullable=False)
    country_id = Column(String(36), ForeignKey("Countries.id"), nullable=False)

    country = relationship("Countries", back_populates="states")
    Companies = relationship("Companies", back_populates="state")
    employees = relationship("Employees", back_populates="state")
