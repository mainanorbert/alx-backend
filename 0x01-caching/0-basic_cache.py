#!/usr/bin/env python3
"""module Create a class BasicCache that
inherits from BaseCaching
and is a caching system"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Class Create a class BasicCache"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
