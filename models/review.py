#!/usr/bin/python3
"""Class to represent user and place."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Inherit from BaseModel."""

    place_id = ''
    user_id = ''
    text = ''
