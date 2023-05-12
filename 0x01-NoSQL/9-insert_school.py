#!/usr/bin/env python3
"""
Contains a function that inserts a new docment in a collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    creates a new dcoument from kwargs and inserts it into
    a collection 'mongo_collcetion'
    """
    return mongo_collection.insert_one(kwargs).inserted_id
