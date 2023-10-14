#!/usr/bin/python3
"""Defines the base model, BaseModel"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the base model from which all subclasses inherit
    Args:
        id (int): The instance uuid
    """
    def __init__(self, *args, **kwargs):
        """Initializes object instance
        Args:
            *args: Takes as many non-keyworded arguments
            **kwargs: Takes as many keyworded arguments
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    time = datetime.strptime(value, time_format)
                    setattr(self, key, time)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now() 

    def __str__(self):
        """String representation of the class instance"""
        return f"[{BaseModel.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute `updated_at`\
                with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary of all keys/values of __dict__\
                of the instance.
        """
        dictcpy = self.__dict__.copy()
        dictcpy.update({"created_at": self.created_at.isoformat()})
        dictcpy.update({"updated_at": self.updated_at.isoformat()})
        dictcpy.update({"__class__": self.__class__.__name__})
        return (dictcpy)
