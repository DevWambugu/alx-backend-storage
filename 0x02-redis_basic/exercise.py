#!/usr/bin/env python3
'''exercise.py'''
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def replay(method: Callable):
    '''This function displays the history of
    calls of a particular function'''
    r_instance = redis.Redis()
    function_name = method.__qualname__
    value = r_instance.get(function_name)
    try:
        value = int(value.decode("utf-8"))
    except Exception:
        '''Assign 0 if there is an error'''
        value = 0
    '''Code to state how many times the function was called'''
    print("{} was called {} times:".format(function_name, value))
    inputs = r_instance.lrange("{}:inputs".format(function_name), 0, -1)
    '''outputs'''
    outputs = r_instance.lrange("{}:outputs".format(function_name), 0, -1)

    '''handle both input and output'''
    for input_, output in zip(inputs, outputs):
        try:
            input_ = input_.decode("utf-8")
        except Exception:
            input_ = ""
        try:
            output_ = output.decode("utf-8")
        except Exception:
            output = ""
        '''Print out'''
        print("{}(*{}) -> {}".format(function_name, input_, output))


def count_calls(method: Callable) -> Callable:
    '''This function takes a single
    method Callable argument and returns a Callable'''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''A wrapper function that takes in a no of
        arguments and key word arguments'''
        key = method.__qualname__
        count_key = f"{key}_call_count"
        self._redis.incr(count_key)
        result = method(self, *args, **kwargs)
        return result
    return wrapper


def call_history(method: Callable) -> Callable:
    '''This decorator to stores the history
    of inputs and outputs for a particular function.'''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''This is the method wrapper'''
        input_key = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input_key)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output
    return wrapper


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

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''This function decorates the Cache.store method
        with count_calls'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
