#!/usr/bin/env python3
"""File storage module.

Handles JSON serializations and deserialization.
"""
import json
import os


class FileStorage:
    """FileStorage class."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Get all objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Create a new object."""
        class_name = str(obj.__class__.__name__)
        FileStorage.__objects[f"{class_name}.{obj.id}"] = obj.to_dict()

    def save(self):
        """Save a new object to json."""
        with open(FileStorage.__file_path, "w") as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        """Reload the objects from json."""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                FileStorage.__objects = dict(json.load(file))
