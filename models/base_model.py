#!usr/bin/python3
"""Defines the BaseModel class."""
import models
import uuid
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
        tformat = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                elif k == "created_at" or k == "updated_at":
                    time = datetime.strptime(v, tformat)
                    setattr(self, k, time)
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """return the print/str representation of the BaseModel instance"""
        clsname = self.__class__.__name__
        return ("[{}] ({}) {}".format(clsname, self.id, self.__dict__))

    def save(self):
        """updates the current datetime after changes"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dict containing all keys/values"""
        dict_rep = {}
        for k, v in self.__dict__.items():
            dict_rep[k] = v
            if isinstance(v, datetime):
                dict_rep[k] = v.strftime('%Y-%m-%dT%H:%M:%S.%f')
        dict_rep["__class__"] = type(self).__name__
        return dict_rep
