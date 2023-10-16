#!/usr/bin/python3
"""
Test module for user class
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
import re
import os
import json
from models import storage
import time


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def setUp(self):
        """Sets test methods"""
        pass

    def tearDown(self):
        """Tears down method"""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_amenity_instantiation(self):
        """Test __init__ method"""
        b = Amenity()
        self.assertEqual(str(type(b)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(b, Amenity)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_amenity_attributes(self):
        """Test Amenity class attributes"""
        attributes = storage.attributes()["Amenity"]
        o = Amenity()
        for key, value in attributes.items():
            self.assertTrue(hasattr(o, key))
            self.assertEqual(type(getattr(o, key, None)), value)


if __name__ == '__main__':
    unittest.main()
