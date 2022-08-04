#!/usr/bin/python3
"""Defines the BaseModel class."""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represent the base model.
    Represents the "base" for all other classes in AirBnB project.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new Base.
        Args:
            *args: as many arguments.
            **kwargs: key/pair value arguments.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    format = "%Y-%m-%dT%H:%M:%S.%f"
                    self.__dict__[k] = datetime.strptime(v, format)
                else:
                    self.__dict__[k] = v

    def __str__(self):
        """return the print/str representation of the BaseModel instance"""
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)

    def save(self):
        """updates the current datetime after changes"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dict containing all key/values"""
        ndict = self.__dict__.copy()
        ndict['created_at'] = self.created_at.isoformat()
        ndict['updated_at'] = self.updated_at.isoformat()
        ndict['__class__'] = self.__class__.__name__
        return ndict
