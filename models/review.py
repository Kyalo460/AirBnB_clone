#!/usr/bin/bash python3
"""Review Model."""

from .base_model import BaseModel


class Review(BaseModel):
    """Review Model.

    - place_id: string - empty string: it will be the Place.id
    - user_id: string - empty string: it will be the User.id
    - text: string - empty string
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Construct Method."""
        super().__init__(*args, **kwargs)
