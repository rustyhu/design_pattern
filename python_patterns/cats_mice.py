"""
observer: cats chasing mice
"""

from abc import ABC, abstractmethod
#import pdb
#import logging

class Mouse():
    def __init__(self, id):
        self._id = id
        self._ob = []
        print("Mouse %d come out from hole!" % self._id)
    
    def id(self):
        return self._id

    def setObserver(self, cat):
        self._ob.append(cat)

    def run(self):
        print("Mouse {} start to run!", self._id)
        for ob in self._ob:
            ob.notify(self._id)
    
class Cat:
    def __init__(self, id):
        self._id = id
        self._watching = []

    def id(self):
        return self._id

    def watch(self, mouse):
        self._watching.append(mouse)
        mouse.setObserver(self)
        print("Cat {} is watching mouse {}!".format(self._id, mouse.id()))
    
    def notify(self, mouseid):
        print("Cat {} is chasing mouse {}!".format(self._id, mouseid))


def execute_pattern():
    mice = []
    for i in range(1, 11):
        mice.append(Mouse(i))
    
    cats = [Cat(30), Cat(31)]
    for m in mice[:5]:
        cats[0].watch(m)
    for m in mice[5:]:
        cats[1].watch(m)

    for m in mice:
        m.run()

if __name__ == '__main__':
    execute_pattern()