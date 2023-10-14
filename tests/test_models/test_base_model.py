#!/usr/bin/python3

import inspect
import models
# import pep8 as pycodestyle
import unittest
import time
from unittest import mock
from datetime import datetime
BaseModel = models.base_model.BaseModel
mdoc = models.base_model.__doc__


class TestBaseModelDocs(unittest.TestCase):
    """Tests to check the documentation and style of BaseModel class"""

    @classmethod
    def setUpClass(self):
        """Setup for docstring tests"""
        self.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

#    def test_pep8_approval(self):
#       """Tests that models/base_model.py conforms to PEP8 standards"""
#        for path in ['models/base_models.py'
#            'tests/test_models/test_base_model.py']:
#          with self.subTest(path=path):
#              errors = pycodestyle.Checker(path).checkall()
#              self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test for existence of module docstring"""
        self.assertIsNot(mdoc, None,
                         "base_model.py has no docstring")
        self.assertTrue(len(mdoc) > 1,
                        "base_model.py has no docstring")

    def test_class_docstring(self):
        """Test for the BaseModel class docstring"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")
