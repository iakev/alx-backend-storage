#!/usr/bin/env python3
"""
contains a function that returns list of schools having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns lists of schools having a topic
    """
    return list(mongo_collection.find({"topics": topic}))
