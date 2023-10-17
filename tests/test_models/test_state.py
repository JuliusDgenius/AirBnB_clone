#!/usr/bin/python3
"""
Test Module for state class
"""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestClass(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
