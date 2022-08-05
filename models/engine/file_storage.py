#!/usr/bin/python3
"""Defines the FileStorage class"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Represents the file storage for AirBnB project.
    Initialize a new Base.
    Args:
    __file_path(str): pathname of file.
    __objects (dict): where objects of the class are stored.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """converts object to JSON and store in file"""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w" as f:
                json.dump(objdict, f))

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
