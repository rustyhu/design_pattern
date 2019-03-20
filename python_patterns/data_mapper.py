"""
Data Mapper
"""

import unittest
#import pdb
#import logging

class User:
    @staticmethod
    def fromState(state):
        return User(state['username'], state['email'])

    def __init__(self, username, email):
        self._username = username
        self._email = email

    @property
    def username(self):
        return self._username
    @property
    def email(self):
        return self._email

class UserMapper:
    def __init__(self, storage):
        self._adapter = storage
    def findById(self, id):
        rst = self._adapter.find(id)
        if not rst:
            raise ValueError
        return self.mapRowToUser(rst)
    def mapRowToUser(self, row):
        return User.fromState(row)

class StorageAdapter:
    def __init__(self, data):
        self._data = data
    def find(self, id):
        if id in self._data:
            return self._data[id]
        return None

class DataMapperTest(unittest.TestCase):
    def testCanMapFromStorage(self):
        storage = StorageAdapter({
            1: {'username': 'domnik', 'email': 'liebler.dominik@gmail.com'}
        })
        mapper = UserMapper(storage)

        user = mapper.findById(1)
        self.assertIsInstance(user, User)
    
    def testInvalidData(self):
        storage = StorageAdapter({})
        mapper = UserMapper(storage)
        with self.assertRaises(ValueError):
            user = mapper.findById(1)

if __name__ == '__main__':
    unittest.main()