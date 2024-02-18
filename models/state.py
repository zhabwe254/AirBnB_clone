#!/usr/bin/python3
"""Module for State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel."""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of State."""
        super().__init__(*args, **kwargs)
