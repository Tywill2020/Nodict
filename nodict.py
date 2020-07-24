#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'Tyrell Williams'


class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.hash = hash(self.key)
        self.value = value

    def __repr__(self):
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        return self.key == other.key


class NoDict:
    def __init__(self, num_buckets=10):
        self.buckets = [[] for _ in range(num_buckets)]
        self.size = num_buckets


    def __repr__(self):
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}' for i, bucket in enumerate(self.buckets)])
        

    def add(self, key, value=None):
        new_node = Node(key, value)
        bucket = self.buckets[new_node.hash % self.size]
        for kv in bucket:
            if kv == new_node:
                bucket.remove(kv)
                break
        bucket.append(new_node)

    def get(self, key):
        key_value = Node(key)
        bucket = self.buckets[key_value.hash % self.size]
        for kv in bucket:
            if kv == key_value:
                return kv.value
        raise KeyError(f'{key} Not Found')

    def __getitem__(self, key):
        value = self.get(key)
        return value

    def __setitem__(self, key, value):
        self.add(key, value)
    
