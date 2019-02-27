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

class DateComparator(ComparatorInterface):
    @staticmethod
    def compare(a, b):
        return a.date > b
    
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
    def __init__(self, name, id, date):
        self._name = name
        self._id = id
        self._date = date
    @property
    def id(self):
        return self._id
    @property
    def date(self):
        return self._date

class StrategyTest(unittest.TestCase):
    def prepare(self):
        # prepare for data ['date']
        self._data = []
        for i in range(10):
            self._data.append(Tobj("samename", i, i+1))

    def testDate(self):

        c = Context(DateComparator, 0)
        result = c.executeStrategy(self._data)
        self.assertEqual(result, [])

    def testId(self):
        # prepare for data ['id']
        c = Context(IdComparator, -1)
        result = c.executeStrategy(self._data)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()