#!/usr/bin/env python3
"""
basic_cache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache defines:
    - derived class from BaseCachin
    - unlimited cache
    """

    def __init__(self):
        """
        initializer
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is not None:
            return self.cache_data.get(key)
        return None

