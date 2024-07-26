#!/usr/bin/env python3
"""
basic_cache module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    LRUCache defines:
    - derived class from BaseCachin
    - LRU cache
    """

    def __init__(self):
        """
        initializer
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to cache using LRU
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
            self.cache_data[key] = item

            if len(self.cache_data) > self.MAX_ITEMS:
                t_key = self.cache_data.popitem(last=False)[0]
                print('DISCARD: {}'.format(t_key))

    def get(self, key):
        """
        Get an item by key
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data.get(key)
        return None
