"""
command
"""

from abc import ABC, abstractmethod
# performance test
import timeit
#import logging

class CommandInterface(ABC):
    def execute(self):
        raise NotImplementedError

class HelloCommand(CommandInterface):
    def __init__(self, console):
        self.output = console
    
    def execute(self):
        self.output.write('Hello World')

class Receiver:
    bDate_ = False
    output = []

    def write(self, sz):
        if self.bDate_:
            sz += ' [' + 'Y-m-d' + ']'
        self.output.append(sz)
    
    def getOutput(self):
        return '\n'.join(self.output)
    
    def enableDate(self):
        self.bDate_ = True
    
    def disableDate(self):
        self.bDate_ = False

class Invoker:
    command = None
    def setCommand(self, cmd):
        self.command = cmd

    def run(self):
        self.command.execute()

if __name__ == '__main__':
    invoker = Invoker()

    # invoker do not need to know details about init and config of these
    # "concrete commands"
    receiver = Receiver()
    receiver.enableDate()

    invoker.setCommand(HelloCommand(receiver))
    invoker.run()
    print(receiver.getOutput())