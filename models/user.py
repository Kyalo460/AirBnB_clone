#!/usr/bin/bash python3
"""User Model."""

from .base_model import BaseModel


class User(BaseModel):
    """User Model.

    - @email: string - empty string
    - @password: string - empty string
    - @first_name: string - empty string
    - @last_name: string - empty string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Construct Method."""
        super().__init__(*args, **kwargs)
