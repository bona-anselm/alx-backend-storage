#!/usr/bin/env python3
""" Defines Cache class """
import redis
import uuid
from typing import Union, Callable


class Cache:
    """ Creates Cache class """
    def __init__(self):
        """ Initializes the Cache instances """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ generates a random key (e.g. using uuid), store the input
            data in Redis using the random key and return the key
        """
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key

    def get(self,
            key: str,
            fn: Callable = None
            ) -> Union[str, int, bytes, float]:
        """ Retrieves values from the Redis data storage """
        self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """ Takes data and converts to string """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """ Takes data and converts to integer """
        return self.get(key, lambda x: int(x))
