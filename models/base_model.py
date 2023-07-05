#!/usr/bin/python3
"""Base model"""
import uuid
import datetime


class BaseModel:
    """Class BaseModel"""

    id = str(uuid.uuid4())
    created_at = datetime.datetime.now()

    updated_at = datetime.datetime.now()

    def __str__(cls):
        return f"[{cls.__class__.__name__}] ({cls.id}) {cls.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(cls):
        new_dict = cls.__dict__.copy()
        new_dict["__class__"] = str(type(cls).__name__)
        new_dict["created_at"] = cls.created_at.isoformat()
        new_dict["updated_at"] = cls.updated_at.isoformat()
        return new_dict
