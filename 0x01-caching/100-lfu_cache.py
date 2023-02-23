#!/usr/bin/env python3
"""crate an inheritable  LFUCache caching system"""


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """A simple caching system that inherits from Basecaching"""

    def __init__(self):
        """the constructor class"""
        super().__init__()
        self.frequency = {}

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
                leastfre = self.frequency[keys[0]]
                leastfrekey = keys[0]
                for frekey, val in self.frequency.items():
                    if val < leastfre:
                        leastfrekey = frekey
                        leastfre = val
                for frekey in self.cache_data.keys():
                    if self.cache_data[frekey] == self.cache_data[leastfrekey]:
                        print("DISCARD: {}".format(frekey))
                        del self.cache_data[frekey]
                        del self.frequency[frekey]
                        break
        self.cache_data[key] = item
        self.frequency[key] = 0

    def get(self, key):
        """get an item"""
        if key is None:
            return (None)
        if key not in self.cache_data.keys():
            return (None)
        val = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data[key] = val
        self.frequency[key] += 1
        return self.cache_data[key]
