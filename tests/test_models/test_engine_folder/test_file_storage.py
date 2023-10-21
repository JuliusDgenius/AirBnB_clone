#!/usr/bin/python3
"""Test module for FileStorage."""

import unittest
import os
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class TestFileStorage(unittest.TestCase):
    """Defines test class for FileStorage"""

    def test_a_attributes(self):
        """Tests filestorage path"""
        self.assertTrue(hasattr(storage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(storage, "_FileStorage__objects"))

    def test_b_all(self):
        """Tests all() method"""
        storage.reload()
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_c_new(self):
        """Tests new method"""
        storage.reload()
        new_object = BaseModel()
        storage.new(new_object)
        all_objects = storage.all()
        self.assertIn(new_object, all_objects.values())

    def test_d_save(self):
        """Tests save() method"""
        temp_path = storage._FileStorage__file_path
        storage._FileStorage__file_path = "temp_file.json"
        storage.reload()
        new_object = BaseModel()
        storage.new(new_object)
        storage.save()
        self.assertTrue(os.path.isfile(storage._FileStorage__file_path))
        os.remove(storage._FileStorage__file_path)

    def test_e_classes(self):
        """Tests classes() method"""
        classes = storage.classes()
        self.assertIsInstance(classes, dict)

    def test_f_reload(self):
        """Tests reload() method"""
        temp_path = storage._FileStorage__file_path
        storage._FileStorage__file_path = "temp_file.json"
        storage.reload()
        new_object = BaseModel()
        storage.new(new_object)
        storage.save()
        storage.reload()
        all_objects = storage.all()
        self.assertIn(new_object, all_objects.values())
        os.remove(storage._FileStorage__file_path)

    def test_g_update(self):
        """Tests update() method"""
        storage.reload()
        new_object = BaseModel()
        storage.new(new_object)
        storage.save()
        new_object_id = new_object.id
        storage.update("BaseModel", new_object_id, "name", "Updated Name")
        updated_object = storage.find("BaseModel", new_object_id)
        self.assertEqual(updated_object.name, "Updated Name")

    def test_h_find(self):
        """Tests find() method"""
        storage.reload()
        new_object = BaseModel()
        storage.new(new_object)
        storage.save()
        new_object_id = new_object.id
        found_object = storage.find("BaseModel", new_object_id)
        self.assertEqual(found_object, new_object)

    def test_i_delete(self):
        """Tests delete() method"""
        storage.reload()
        new_object = BaseModel()
        storage.new(new_object)
        storage.save()
        new_object_id = new_object.id
        deleted_object = storage.delete("BaseModel", new_object_id)
        self.assertNotIn(deleted_object, storage.all().values())

    def test_j_attributes(self):
        """Tests attribute() method"""
        attributes = storage.attributes()
        self.assertIsInstance(attributes, dict)

if __name__ == '__main__':
    unittest.main()

