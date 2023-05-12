#!/usr/bin/env python3
"""
Containd a function that updates a document in a collection
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name
    """
    if topics:
        mongo_collection.find_one_and_update(
            {'name': name}, {'$set': {'topics': topics}})
