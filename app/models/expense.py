#!/usr/bin/python3
"""expense collection module"""

from .base_model import BaseModel


class Expense(BaseModel):
    """expense collection class"""
    def __init__(self):
        super().__init__("expense")  # collection name
    
    def create_expense(self, budget_id, category, amount):
        """create document / object"""
        return self.save({
            "budget_id": budget_id,
            "category": category,
            "amount": amount
        })
