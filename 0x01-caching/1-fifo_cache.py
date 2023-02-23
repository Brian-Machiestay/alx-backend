#!/usr/bin/env python3
"""crate an inheritable FIFO caching system"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
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
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            keys = [key for key in self.cache_data.keys()]
            print("DISCARD: {}".format(keys[0]))
            del self.cache_data[keys[0]]
        self.cache_data[key] = item

    def get(self, key):
        """get an item"""
        if key is None:
            return (None)
        if key not in self.cache_data.keys():
            return (None)
        return self.cache_data[key]
