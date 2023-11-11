#!/usr/bin/bash python3
"""State Model."""

from .base_model import BaseModel


class State(BaseModel):
    """State Model.

    - name: string - empty string
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Construct Method."""
        super().__init__(*args, **kwargs)
