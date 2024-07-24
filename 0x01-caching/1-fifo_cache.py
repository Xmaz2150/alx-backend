#!/usr/bin/env python3
"""
basic_cache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache defines:
    - derived class from BaseCachin
    - FIFO cache
    """

    def __init__(self):
        """
        initializer
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to cache using FIFO
        """
        if key is not None and item is not None:
            cache_view = [key for key in self.cache_data.keys()]

            if len(cache_view) == self.MAX_ITEMS and \
                    key not in self.cache_data:
                self.cache_data.pop(cache_view[0])
                print('DISCARD: {}'.format(cache_view[0]))
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is not None:
            return self.cache_data.get(key)
        return None

