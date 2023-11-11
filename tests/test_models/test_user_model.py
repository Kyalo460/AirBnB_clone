#!/usr/bin/python3
"""Test for the FileStorage class."""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test for the FileStorage Class."""

    def test_attributes(self):
        """Test the User class attributes."""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_inheritance(self):
        """Test that User inherits from BaseModel."""
        user = User()
        self.assertTrue(issubclass(User, BaseModel))
        self.assertTrue(isinstance(user, BaseModel))

    def test_to_dict(self):
        """Test the to_dict() method."""
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertTrue('id' in user_dict)
        self.assertTrue('created_at' in user_dict)
        self.assertTrue('updated_at' in user_dict)

    def test_from_dict(self):
        """Test creating a User instance from a dictionary."""
        user_data = {
            '__class__': 'User',
            'id': '12345',
            'created_at': '2023-10-17T12:34:56.789012',
            'updated_at': '2023-10-17T12:34:56.789012',
            'email': 'user@example.com',
            'password': 'secret',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        user = User(**user_data)
        self.assertEqual(user.id, '12345')
        self.assertEqual(user.email, 'user@example.com')
        self.assertEqual(user.password, 'secret')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')
