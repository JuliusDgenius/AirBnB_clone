#!/usr/bin/python3
"""Defines the FileStorage class"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


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
        """deserializes the JSON file to __objects"""

        file = FileStorage.__file_path
        if not os.path.exists(file):
            return
        try:
            with open(file, mode="r+", encoding="utf-8") as f:
                file_string = f.read()
                data = json.loads(file_string)
                for object_key, model_data in data.items():
                    model_name, model_id = object_key.split('.')
                    model = models.classes[model_name](**model_data)
                    self.new(model)

        except Exception as e:
            print(e)

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
