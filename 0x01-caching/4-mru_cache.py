#!/usr/bin/python3
"""module for MRU Caching"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """class MRUCache that inherits
    from BaseCaching and is a
    caching system"""
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                lru_k = self.order[-1]
                del self.cache_data[lru_k]
                print(f"DISCARD: {lru_k}")
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        if key is None or key not in self.cache_data.keys():
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
