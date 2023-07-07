#!/usr/bin/python3
"""Base model"""
import uuid
import datetime
from models.__init__ import storage


class BaseModel:
    """Class BaseModel"""

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        #if kwargs:
         #   for key, value in kwargs.items():
          #      if not key == "__class__":
          #          setattr(self, key, value)
        #else:
         #   storage.new(self)

    def __str__(self):
        """print"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute 'updated_at' \
            with the current datetime"""
        storage.save()
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = str(type(self).__name__)
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
