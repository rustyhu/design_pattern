"""
Visitor
"""

from abc import ABC, abstractmethod
import unittest
#import pdb
#import logging

class RoleVistiorIf(ABC):
    def visitUser(self, role):
        raise NotImplementedError
    def visitGroup(self, role):
        raise NotImplementedError

class RoleVisitor(RoleVistiorIf):
    def __init__(self):
        self._visited = []
    def visitUser(self, role):
        self._visited.append(role)
    def visitGroup(self, role):
        self._visited.append(role)
    def getVisited(self):
        return self._visited

class Role(ABC):
    def accept(self, visitor: RoleVistiorIf):
        raise NotImplementedError

class User(Role):
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return "User %s" % self._name
    def accept(self, visitor):
        visitor.visitUser(self)
    def __str__(self):
        return "User Role: {}\n".format(self._name)

class Group(Role):
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return "Group %s" % self._name
    def accept(self, visitor: RoleVistiorIf):
        visitor.visitGroup(self)
    def __str__(self):
        return "Group Role: {}\n".format(self._name)

class VisitorTest(unittest.TestCase):
    def setUp(self):
        self._visitor = RoleVisitor()
    def setRoles(self, n):
        for i in range(n):
            role = User(str(i))
            if self._visitor:
                role.accept(self._visitor)
    def setGroups(self, n):
        for i in range(n):
            role = Group(str(i))
            if self._visitor:
                role.accept(self._visitor)

    def testVisitSomeRole(self):
        self.setUp()
        self.setRoles(2)
        self.setGroups(5)

        print(*self._visitor.getVisited())
        #self.assertEqual("", "")

if __name__ == '__main__':
    unittest.main()