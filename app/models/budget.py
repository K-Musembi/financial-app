#!/usr/bin/python3
"""budget collection module"""

from .base_model import BaseModel


class Budget(BaseModel):
    """budget collection class"""
    def __init__(self):
        """create collection"""
        super().__init__("budget")  # collection name
    
    def create_budget(self, user_id, period, amount):
        """create document / object"""
        return self.save({
            "user_id": user_id,
            "period": period,
            "amount": amount
        })
