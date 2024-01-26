#!/usr/bin/env python3
'''exercise.py'''
import redis
import uuid
from typing import Union


class Cache:
    '''This class contains a method
    to store data in redis'''
    def __init__(self, host='localhost', port=6379, db=0):
        '''stores an instance of the Redis client.
        it also flushes the instance'''
        self._redis = redis.Redis(host=host, port=port, db=db)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''takes the argument data and returns a string'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
