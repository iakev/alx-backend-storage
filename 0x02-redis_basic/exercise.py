#!/usr/bin/env python3
"""
Creating a cache class that writes string data type to Redis
"""
import redis
from typing import Union
import uuid


class Cache:
    """
    class describing the cache class and writing strings to Redis
    """
    def __init__(self):
        """
        Initialising an instance of Redis client
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Takes in a data, generates an uuid to be used as a key
        storing data as input value and returns the key as a
        string
        """
        key = uuid.uuid4()
        key = str(key)
        self._redis.set(key, data)
        return key
