#!/usr/bin/python3
"""FIFO caching"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """class FIFOCache that inherits
    from BaseCaching and is a
    caching system"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                my_key = next(iter(self.cache_data))
                del self.cache_data[my_key]
                print(f"DISCARD: {my_key}")
            self.cache_data[key] = item

    def get(self, key):
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
