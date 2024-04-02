#!/usr/bin/python3
"""module for MRU Caching"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """class MRUCache that inherits
    from BaseCaching and is a
    caching system"""
    def __init__(self):
        """initializing data"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """caching data"""
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                mru_k = self.order[-1]
                del self.cache_data[mru_k]
                print(f"DISCARD: {mru_k}")
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """getting  cached data"""
        if key is None or key not in self.cache_data.keys():
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
