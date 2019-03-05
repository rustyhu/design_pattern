"""
Memento 
"""

from abc import ABC, abstractmethod
import copy
import unittest
#import pdb
#import logging

class SpecificationInterface(ABC):
    @abstractmethod
    def isSatisfiedBy(self, item):
        raise NotImplementedError
    
class OrSpecification(SpecificationInterface):
    def __init__(self, *specifications):
        self._specs = specifications
    def isSatisfiedBy(self, item):
        "match either spec, or logic"
        for spec in self._specs:
            if spec.isSatisfiedBy(item):
                return True
        return False

class AndSpecification(SpecificationInterface):
    def __init__(self, *specifications):
        self._specs = specifications
    def isSatisfiedBy(self, item):
        "must match all specs, and logic"
        for spec in self._specs:
            if not spec.isSatisfiedBy(item):
                return False
        return True

class NotSpecification(SpecificationInterface):
    def __init__(self, spec):
        self._spec = spec
    
    def isSatisfiedBy(self, item):
        "Not logic"
        return not self._spec.isSatisfiedBy(item)

class PriceSpecification(SpecificationInterface):
    def __init__(self, minPrice, maxPrice):
        self._max = maxPrice
        self._min = minPrice
    def isSatisfiedBy(self, item):
        if item:
            return item.price > self._min and item.price < self._max
        else:
            return False

class Item:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

class SpecificationTest(unittest.TestCase):
    def testOr(self):
        spec1 = PriceSpecification(50, 99)
        spec2 = PriceSpecification(101, 200)

        or_spec = OrSpecification(spec1, spec2)
        self.assertFalse(or_spec.isSatisfiedBy(Item(100)))
        self.assertTrue(or_spec.isSatisfiedBy(Item(70)))
    
    def testAnd(self):
        spec1 = PriceSpecification(60, 100)
        spec2 = PriceSpecification(90, 200)

        a_specs = AndSpecification(spec1, spec2)
        self.assertTrue(a_specs.isSatisfiedBy(Item(95)))
        self.assertFalse(a_specs.isSatisfiedBy(Item(70)))

if __name__ == '__main__':
    unittest.main()