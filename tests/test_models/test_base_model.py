#!/usr/bin/python3
"""Test for the base model."""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test for the BaseModel."""

    def setUp(self):
        """Test Construct."""
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def test_base_model_init(self):
        """Test creating a new instance with no arguments."""
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)

    def test_attr_types(self):
        """Test BaseModel instance attribute types."""
        self.assertEqual(str, type(self.my_model.id))
        self.assertEqual(datetime, type(self.my_model.created_at))

    def test_updated_at(self):
        """Test the updated_at attribute."""
        self.my_model.save()
        self.assertNotEqual(self.my_model.created_at, self.my_model.updated_at)

    def test_base_model_dict(self):
        """Test the dict to base model."""
        my_model_json = self.my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)

        self.assertEqual(type(my_new_model.created_at), datetime)
        self.assertNotEqual(self.my_model, my_new_model)

    def test_base_model_init_with_dict(self):
        """Test creating an instance with a dictionary representation."""
        data = {
            "id": "test_id",
            "created_at": "2023-01-01T00:00:00",
            "updated_at": "2023-01-02T00:00:00",
            "name": "Test Model"
        }
        model = BaseModel(**data)
        self.assertEqual(model.id, "test_id")
        self.assertEqual(model.created_at.year, 2023)
        self.assertEqual(model.name, "Test Model")

    def test_base_model_save(self):
        """Test the save method."""
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(original_updated_at, model.updated_at)

    def test_base_model_to_dict(self):
        """Test the to_dict method."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertTrue(isinstance(model_dict, dict))
        self.assertEqual(model_dict['__class__'], 'BaseModel')

    def test_base_model_str(self):
        """Test the __str__ method."""
        model = BaseModel()
        model_str = str(model)
        self.assertIn("BaseModel", model_str)
        self.assertIn(model.id, model_str)
