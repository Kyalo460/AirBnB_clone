#!/usr/bin/bash python3
"""Amenity Model."""

from .base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Model.

    - name: string - empty string
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Construct Method."""
        super().__init__(*args, **kwargs)
