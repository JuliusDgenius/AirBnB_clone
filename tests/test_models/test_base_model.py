#!/usr/bin/python3
"""Test module for BaseModel class"""

from models.base_model import BaseModel
import unittest
from datetime import datetime
from unittest import mock


class TestBaseModel(unittest.TestCase):
    """Defines the test cases for the BaseModel class"""

    def setUp(self):
        """Sets up the test methods"""
        self.my_obj = BaseModel()

    def tearDown(self):
        """Tear down method"""
        del self.my_obj

    def test_id_instantiation(self):
        my_obj = BaseModel()
        self.assertIs(type(my_obj.id), str)

    def test_diff_ID_instances(self):
        my_obj = BaseModel()
        my_obj1 = BaseModel()
        self.assertNotEqual(my_obj.id, my_obj1.id)

    def test_created_at(self):
        my_obj = BaseModel()
        self.assertIs(type(my_obj.created_at), str)

    def test_created_at(self):
        my_obj = BaseModel()
        created_at = my_obj.created_at
        updated_at = my_obj.updated_at
        self.assertNotEqual(updated_at, created_at)

    def test_instance_BaseModel(self):
        my_obj = BaseModel()
        self.assertIsInstance(my_obj, BaseModel)

    def test_str_method(self):
        """Tests the __str__ method"""
        my_obj = BaseModel()
        s = "[{}] ({}) {}".format(my_obj.__class__.__name__,
                                  my_obj.id, my_obj.__dict__)
        self.assertEqual(str(my_obj), s)

    def test_dict_method(self):
        """Tests the dict method"""
        my_obj = BaseModel()
        dct = my_obj.to_dict()
        self.assertEqual(dct["__class__"], "BaseModel")
        self.assertEqual(type(dct["created_at"]), str)
        self.assertEqual(type(dct["updated_at"]), str)

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for json"""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        d = my_model.to_dict()
        expected_attrs = ["id", "created_at", "updated_at", "name",
                          "my_number", "__class__"]
        self.assertCountEqual(d.keys(), expected_attrs)
        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertEqual(d['name'], "My_First_Model")
        self.assertEqual(d['my_number'], 89)

    def test_save(self):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        inst = BaseModel()
        old_created_at = inst.created_at
        old_updated_at = inst.updated_at
        inst.save()
        new_created_at = inst.created_at
        new_updated_at = inst.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)


if __name__ == "__main__":
    TestBaseModel()
