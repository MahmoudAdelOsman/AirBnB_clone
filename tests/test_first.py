#!/usr/bin/env python3
import unittest
from models.base_model import BaseModel
import datetime

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def test_id_is_string(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(original_updated_at, self.base_model.updated_at)

    def test_to_dict_returns_dict(self):
        result = self.base_model.to_dict()
        self.assertIsInstance(result, dict)

    def test_to_dict_contains_class_name(self):
        result = self.base_model.to_dict()
        self.assertIn('__class__', result)
        self.assertEqual(result['__class__'], 'BaseModel')

    def test_to_dict_contains_created_at(self):
        result = self.base_model.to_dict()
        self.assertIn('created_at', result)

    def test_to_dict_contains_updated_at(self):
        result = self.base_model.to_dict()
        self.assertIn('updated_at', result)

if __name__ == '__main__':
    unittest.main()
