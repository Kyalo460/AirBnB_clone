#!/usr/bin/env python3
"""Base Model module.

This module contains the BaseModel class
that defines all common attributes/methods for other classes.
"""
import uuid
from datetime import datetime
from . import storage


class BaseModel:
    """BaseModel Definition.

    This defines all common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """Construct Method."""
        if len(kwargs) == 0:
            # new instance
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

        else:
            # instance with a dictionary representation
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    # converts created_at and updated_at from str to datetime.
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != "__class__":
                    # skip the __class__ attribute.
                    setattr(self, key, value)

    def save(self):
        """Save method updates the public instance attribute updated_at."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """to_dict returns the dictionary rep of the instance."""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict["created_at"] = str(self.created_at.isoformat())
        new_dict["updated_at"] = str(self.updated_at.isoformat())
        return new_dict

    def __str__(self):
        """__str__ method returns the string representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
