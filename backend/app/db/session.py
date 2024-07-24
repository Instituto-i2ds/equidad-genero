from fastapi import Depends
from sqlalchemy.orm import Session

from .database import localSession

def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()

