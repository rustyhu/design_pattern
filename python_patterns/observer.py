"""
observer
"""

from abc import ABC, abstractmethod
import timeit
#import logging

#could be rewritten as ABC
class User:
    def __init__(self, name):
        self.name_ = name
        self.status_ = ''
        self.observers = []
    
    def attach(self, ob):
        self.observers.append(ob)

    def detach(self, ob):
        self.observers.remove(ob)

    @property
    def name(self):
        return self.name_

    @property
    def status(self):
        return self.status_
    
    @status.setter
    def status(self, nstat):
        self.status_ = nstat
        self.notify()
    
    def notify(self):
        for o in self.observers:
            o.update(self)
    
class UserObserver:
    def __init__(self, name):
        self.name_ = name
        self.statuses_ = dict()

    def update(self, c):
        #self.statuses_[c.name] = c.status
        #for (k, v) in self.statuses_.items():
        print(f"Observer{self.name_} reporting: user{c.name} nofity its new state {c.status};")

if __name__ == '__main__':
    sub1 = User('s1')
    sub2 = User('s2')
    sub3 = User('s3')

    obA = UserObserver('A')
    obB = UserObserver('B')
    #obC = UserObserver('C')

    # make group
    sub1.attach(obA)
    sub2.attach(obB)

    sub3.attach(obA)
    sub3.attach(obB)

    i = 100
    for ele in [sub1, sub2, sub3]:
        ele.status = i
        i += 100