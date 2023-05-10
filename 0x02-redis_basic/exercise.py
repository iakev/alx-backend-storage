#!/usr/bin/env python3
"""
Creating a cache class that writes string data type to Redis
"""
import redis
from typing import Any, Callable, Union
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

    def get(self, key: str, fn: Callable[[Any], Union[str, int, None]]) -> Union[str, int, None]:
        """
        Takes in key, fn which is used to convert data back to desired format
        """
        val = self._redis.get(key)
        if fn == int:
            print(f"get int called")
            val = self.get_int(val)
        elif fn == str:
            print("get str supposed to be called")
            val = self.get_str(val)
        elif fn:
            print(f"lamda called")
            val = fn(val)            
        return val

    def get_str(val: bytes) -> str:
        """
        converts byte string representation to a str and returns it
        """
        return str(decoded)

    def get_int(self, val: bytes) -> int:
        """
        converts byte string representation to an int and returns it
        """
        return int(val)
