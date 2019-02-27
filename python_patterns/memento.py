"""
Memento 
"""

from abc import ABC, abstractmethod
import copy
#import pdb
#import logging

class Memento():
    def __init__(self, stateToSave):
        self._state = stateToSave

    @property
    def state(self):
        return self._state

class State:
    STATE_CREATED = 'created'
    STATE_OPENED = 'opened'
    STATE_ASSIGNED = 'assigned'
    STATE_CLOSED = 'closed'
    # class static attribute?
    _STATES = [
        STATE_CREATED,
        STATE_OPENED, 
        STATE_ASSIGNED,
        STATE_CLOSED,
    ]

    def __init__(self, state):
        self.ensureIsValidState(state)
        self._state = state
    
    @classmethod
    def ensureIsValidState(cls, state):
        if state not in cls._STATES:
            raise TypeError
    
    def __repr__(self):
        return self._state

class Ticket():
    def __init__(self):
        self._current = State(State.STATE_CREATED)

    def open(self):
        self._current = State(State.STATE_OPENED)

    def assign(self):
        self._current = State(State.STATE_ASSIGNED)
    
    def close(self):
        self._current = State(State.STATE_CLOSED)
    
    def saveToMemento(self):
        return Memento(self._current)

    def restoreFromMemento(self, memto):
        self._current = memto.state
    
    def getState(self):
        return self._current

if __name__ == '__main__':
    t = Ticket()
    t.open()

    meme = t.saveToMemento()
    t.assign()
    print(t.getState())
    print(meme.state)

    t.restoreFromMemento(meme)
    print(t.getState())