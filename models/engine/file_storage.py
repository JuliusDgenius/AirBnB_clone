#!/usr/bin/python3
"""Defines the FileStorage class"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represents the file storage for AirBnB project.
    Initialize a new Base.
    Args:
    __file_path(str): pathname of file.
    __objects (dict): where objects of the class are stored.
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """init method"""
        super().__init__()

    def all(self):
        """returns the dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """converts object to JSON and store in file"""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
                json.dump(objdict, f)

    def save(self):
        """converts object to JSON and store in file"""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """converts back to object if file exist"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return

    def update(self, obj_name, obj_id, attr, value):
        """updates object with id 'obj_id'"""
        model = self.__objects["{}.{}".format(obj_name, obj_id)]
        setattr(model, attr, value)

    def find(self, obj_name, obj_id):
        """find object with id 'obj_id'"""
        return self.__objects["{}.{}".format(obj_name, obj_id)]

    def delete(self, obj_name, obj_id):
        """deletes object with id 'obj_id'"""
        return self.__objects.pop("{}.{}".format(obj_name, obj_id))
