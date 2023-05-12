#!/usr/bin/env python3
"""
Module contains a function that lists all documentatoin in a colection
"""


def list_all(mongo_collection):
    """
    lists and returns all documents in mongo_collcetion
    if mongo_collection is empty we return an empty list
    """
    docs = mongo_collection.find()
    return list(docs)
