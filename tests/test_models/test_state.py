#!/usr/bin/python3
"""
Test file for user class
"""

import unittest
from models.state import State
from mdoels.base_model import BaseModel


class TestClass(unittest.TesCase):
    """Test cases"""

    def test_create_instance(self):
        """create a new instance"""
        new_state = State()
        self.assertIsInstance(new_state, State)

    def test_create_instance2(self):
        """create a new instance"""
        new_state = State()
        self.assertIsiInstance(new_state, State)

    def test_create_instance2(self):
        """create a new instance"""
        new_state = State()
        self.assertIsInstance(new_state, BaseModel)


id __name__ == '__main__':
    unittest.main()
