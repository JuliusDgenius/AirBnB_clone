#!/usr/bin/python3
"""Defines the FileStorage class"""

import json
import os
import datetime


class FileStorage:
    """Encodes objects to a JSON file and decodes JSON to instances
    Args:
    __file_path(str): Private attribute pathname of file.
    __objects (dict): Stores all objects.
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """initializes class instance"""
        super().__init__()

    def all(self):
        """returns the dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        k = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[k] = obj

    def save(self):
        """converts object to JSON and store in file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            dct = {key: value.to_dict() for key, value in
                      FileStorage.__objects.items()}
            json.dump(dct, f)

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """deserializes the JSON file to __objects"""

        file = FileStorage.__file_path
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            ob_dict = json.load(f)
            ob_dict = {key: self.classes()[val["__class__"]](**val)
                        for key, val in ob_dict.items()}
            FileStorage.__objects = ob_dict

    def update(self, obj_name, obj_id, attr, value):
        """updates object with id 'obj_id"""
        model = self.__objects["{}.{}".format(obj_name, obj_id)]
        setattr(model, attr, value)

    def find(self, obj_name, obj_id):
        """find object with id 'obj_id"""
        return self.__objects["{}.{}".format(obj_name, obj_id)]

    def delete(self, obj_name, obj_id):
        """deletes object with id 'obj_id"""
        return self.__objects.pop("{}.{}".format(obj_name, obj_id))
