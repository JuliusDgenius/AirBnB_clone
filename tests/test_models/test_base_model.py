#!/usr/bin/python3
"""Test module for BaseModel class"""

from models.base_model import BaseModel
import unittest
from datetime import datetime


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
        self.assertTrue(my_obj.id)

    def test_name_instantiation(self):
        my_obj = BaseModel()
        my_obj.name = "My First Model"
        self.assertEqual(my_obj.name, "My First Model")

    def test_created_at(self):
        my_obj = BaseModel()
        self.assertTrue(my_obj.created_at)

    def test_created_at(self):
        my_obj = BaseModel()
        created_at = my_obj.created_at
        updated_at = my_obj.updated_at
        self.assertNotEqual(updated_at, created_at)

    def test_instance_BaseModel(self):
        my_obj = BaseModel()
        self.assertIsInstance(my_obj, BaseModel)
