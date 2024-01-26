#!/usr/bin/env python3
'''exercise.py'''
import redis
import uuid
from typing import Union, Callable


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

    '''union = Union[str, bytes, int, float] = None'''
    '''fn_ = Callable[[Union[str, bytes, int, float]], union]'''

    def get(self, key: str, fn: Callable[[Union[str, bytes, int, float]], Union[str, bytes, int, float]] = None) -> Union[str, bytes, int, float]:
        ''' This function create a get method that
        take a key string argument and an optional
        Callable argument named fn. This callable will be
        used to convert the data back to the desired format.'''
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        '''This function automatically parametrize
        Cache.get with the correct conversion function'''
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        '''This function also automatically parametrize
        Cache.get with the correct conversion function'''
        return self.get(key, fn=int)
