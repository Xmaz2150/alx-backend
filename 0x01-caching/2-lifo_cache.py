#!/usr/bin/env python3
"""
basic_cache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache defines:
    - derived class from BaseCachin
    - LIFO cache
    """

    def __init__(self):
        """
        initializer
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to cache using LIFO
        """
        if key is not None and item is not None:
            cache_view = [key for key in self.cache_data.keys()]

            if len(cache_view) == self.MAX_ITEMS and \
                    key not in self.cache_data:
                self.cache_data.pop(cache_view[-1])
                print('DISCARD: {}'.format(cache_view[-1]))
            elif key in self.cache_data:
                idx = cache_view.index(key)
                self.cache_data.pop(cache_view[idx])

            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is not None:
            return self.cache_data.get(key)
        return None

