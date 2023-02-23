#!/usr/bin/env python3
"""crate an inheritable  MRUCache caching system"""


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """A simple caching system that inherits from Basecaching"""

    def __init__(self):
        """the constructor class"""
        super().__init__()

    def put(self, key, item):
        """put an item into the cache"""
        if key is None:
            return
        if item is None:
            return
        cache_len = len(self.cache_data)
        if key not in self.cache_data.keys():
            if cache_len + 1 > BaseCaching.MAX_ITEMS:
                keys = [key for key in self.cache_data.keys()]
                if key not in self.cache_data.keys():
                    print("DISCARD: {}".format(keys[cache_len - 1]))
                del self.cache_data[keys[cache_len - 1]]
        self.cache_data[key] = item

    def get(self, key):
        """get an item"""
        if key is None:
            return (None)
        if key not in self.cache_data.keys():
            return (None)
        val = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data[key] = val
        return self.cache_data[key]
