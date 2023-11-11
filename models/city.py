#!/usr/bin/bash python3
"""City Model."""

from .base_model import BaseModel


class City(BaseModel):
    """City Model.

    - state_id: string - empty string
    - name: string - empty string
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Construct Method."""
        super().__init__(*args, **kwargs)
