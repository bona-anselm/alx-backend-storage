#!/usr/bin/env python3
""" Defines Cache class """
import redis
import uuid
from typing import Union


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
