#!/usr/bin/python3
"""base model module"""
from django.conf import settings
from bson.objectid import ObjectId
from datetime import datetime


class BaseModel:
    """base model class"""
    def __init__(self, collection):
        """initialize collection"""
        self.collection = settings.DATABASE_CLIENT[collection]
    
    def save(self, data):
        """create document / object"""
        data['created_at'] = datetime.now(datetime.timezone.utc)
        data['updated_at'] = datetime.now(datetime.timezone.utc)
        return self.collection.insert_one(data)
    
    def find(self, query):
        """find documents marching query"""
        return list(self.collection.find(query))
    
    def find_one(self, query):
        """search for single document"""
        return self.collection.find_one(query)
    
    def update(self, query, update_data):
        """update document"""
        update_data['updated_at'] = datetime.now(datetime.timzone.utc)
        return self.collection.update_one(query, {'$set': update_data})
    
    def delete(self, query):
        """delete document"""
        return self.collection.delete_one(query)
