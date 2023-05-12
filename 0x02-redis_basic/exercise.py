#!/usr/bin/env python3
"""
Creating a cache class that writes string data type to Redis
"""
import functools
import redis
from typing import Any, Callable, Union
import uuid


def count_calls(method: Callable) -> Callable:
    """
    Creates a wrapper_function function that increments count and returns
    the function
    """
    @functools.wraps(method)
    def wrapper_decorator(*args, **kwargs):
        """
        Function that increments count for key
        (func.__qualname__) every time the method is called
        """
        key = method.__qualname__
        self = args[0]
        self._redis.incr(key, amount=1)
        value = method(*args, **kwargs)
        return value
    return wrapper_decorator


def call_history(method: Callable) -> Callable:
    """
    stores history of inputs and outputs for a method
    """
    @functools.wraps(method)
    def wrapper_decorator(*args, **kwargs):
        """
        Creates inputs and outputs lists
        """
        inputs = method.__qualname__ + ":inputs"
        outputs = method.__qualname__ + ":outputs"
        self = args[0]
        new_args = str(args[1:])
        self._redis.rpush(inputs, new_args)
        value = method(*args, **kwargs)
        self._redis.rpush(outputs, value)
        return value
    return wrapper_decorator


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

    @call_history
    @count_calls
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

    def get(self, key: str,
            fn: Callable[[Any],
                         Union[str, int, None]]
            = None) -> Union[str, int, None]:
        """
        Takes in key, fn which is used to convert data back to desired format
        """
        val = self._redis.get(key)
        if not val:
            return None
        if fn == int:
            val = self.get_int(val)
        elif fn == str:
            val = self.get_str(val)
        elif fn:
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


def replay(cache: Cache, method: Callable) -> None:
    """
    Display history of calls of a particular function
    """
    count_key = method.__qualname__
    inputs_key = method.__qualname__ + ":inputs"
    outputs_key = method.__qualname__ + ":outputs"

    count = cache._redis.get(count_key)
    if count is None:
        count = 0
    else:
        count = int(count)
    print(f"{count_key} was called {count} times:")
    for inputs, outputs in zip(cache._redis.lrange(inputs_key, 0, -1),
                               cache._redis.lrange(outputs_key, 0, -1)):
        inputs = inputs.decode('utf-8')
        outputs = outputs.decode('utf-8')
        print(f"{count_key}(*{inputs}) -> {outputs}")
