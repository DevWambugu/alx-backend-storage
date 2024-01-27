#!/usr/bin/env python3
'''web.py'''
import requests
import redis
from functools import wraps
import time

def cache_the_count(expires=10):
    '''This function caches the HTML result and sets
    an expiry period of 10'''
    def decorator(func)
        '''the decorator function'''
        @wraps(func):
        def wrapper(url):
            '''Write the wrapper function
            start by writing the redis connection'''
            r = redis.StrictRedis(host='localhost', port=6379, db=0)
            '''Check if the result is cached'''
            cached_result = r.get(f"cache:{url}")
            if cached_result:
                r.incr(f"count:{url}")
                return cached_result.decode('utf-8')
            '''if not cached, proceed as follows'''
            result = func(url)
            r.setex(f"cache:{url}", expires, result)
            r.incr(f"count:{url}")
            return result
        return wrapper
    return decorator

@cache_the_count()
def get_page(url: str) -> str:
    '''This function uses the requests module to
    obtain the HTML content of a particular URL and returns it'''
    response = requests.get(url)
    return response.text
