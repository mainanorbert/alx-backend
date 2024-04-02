#!/usr/bin/python3
"""module for  LIFO Caching"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Create a class LIFOCache that
    inherits from BaseCaching and is
    a caching system"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                my_key, my_value = self.cache_data.popitem()
                print(f"DISCARD: {my_key}")
            self.cache_data[key] = item

    def get(self, key):
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
