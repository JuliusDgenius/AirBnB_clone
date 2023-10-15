#!/usr/bin/python3
"""This module defines the BaseModel class."""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Represents the parent class for all other classes in AirBnB project.
    """

    def __init__(self, *args, **kwargs):
        """Initialize instances of the BaseModel class..
        Args:
            *args: as many keyworded arguments passed.
            **kwargs: key/value pair arguments as passed.
        """
        if kwargs is not None and kwargs != {}:
            for k in kwargs:
                if k == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif k == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[k] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """return the string rep of the BaseModel instance"""
        clsname = self.__class__.__name__
        return ("[{}] ({}) {}".format(clsname, self.id, self.__dict__))

    def save(self):
        """updates the current datetime after changes"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dict containing all key/value pairs"""
        ndict = self.__dict__.copy()
        ndict["__class__"] = type(self).__name__
        ndict["created_at"] = ndict["created_at"].isoformat()
        ndict["updated_at"] = ndict["updated_at"].isoformat()

        return (ndict)
