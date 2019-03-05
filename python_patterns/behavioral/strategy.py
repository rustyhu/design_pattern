"""
Strategy 
"""

from abc import ABC, abstractmethod
import unittest
#import pdb
#import logging

class ComparatorInterface(ABC):
    @staticmethod
    def compare(a, b) -> bool:
        raise NotImplementedError

class RecordComparator(ComparatorInterface):
    @staticmethod
    def compare(a, b):
        return a.record > b
    
class IdComparator(ComparatorInterface):
    @staticmethod
    def compare(a, b):
        return a.id > b

class Context:
    def __init__(self, comparator: ComparatorInterface, standard):
        self._comparator = comparator
        self._standard = standard
    def executeStrategy(self, elements: list):
        return [e for e in elements if self._comparator.compare(e, self._standard)]

class Tobj:
    def __init__(self, name, id, record):
        self._name = name
        self._id = id
        self._record = record
    @property
    def id(self):
        return self._id
    @property
    def record(self):
        return self._record

class StrategyTest(unittest.TestCase):
    def prepare(self):
        # prepare for data
        self._data = []
        for i in range(-5, 5):
            self._data.append(Tobj("samename", i, i+1))

    def testId(self):
        self.prepare()
        c = Context(IdComparator, -1)
        result = c.executeStrategy(self._data)
        self.assertEqual(result, self._data[-5:])

    def testRecord(self):
        self.prepare()
        c = Context(RecordComparator, 0)
        result = c.executeStrategy(self._data)
        self.assertEqual(result, self._data[-5:])

if __name__ == '__main__':
    unittest.main()