#!/usr/bin/python3
"""user collection module"""

from .base_model import BaseModel
from werkzeug.security import generate_password_hash


class User(BaseModel):
    """user collection class"""
    def __init__(self):
        """create collection"""
        super().__init__("user")  # collection name
    
    def create_user(self, name, email, password):
        """create user document / object"""
        return self.save({
            "name": name,
            "email": email,
            "password": generate_password_hash(password)
        })
