#!/usr/bin/env python3
"""MRU Caching"""

from msilib.schema import Class
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """class MRUCache inherits BaseCaching"""

    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.stack:
                last = self.stack.pop()
                del self.cache_data[last]
                print("DISCARD: {}".format(last))

        if key not in self.stack:
            self.stack.append(key)
        else:
            self.mv_last_item(key)

    def get(self, key):
        """get an item by key"""
        return self.cache_data(key, None)

    def mv_last_item(self, item):
        """moves element to last idx of list"""
        length = len(self.stack)
        if self.stack[length - 1] != item:
            self.stack.remove(item)
            self.stack.append(item)
