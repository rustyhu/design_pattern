"""
Mediator 中介（多边协调者）
"""

from abc import ABC, abstractmethod
# performance test
import time
#import logging

class MediatorIf(ABC):
    @abstractmethod
    def sendResponse(self, content):
        raise NotImplementedError
    @abstractmethod
    def makeRequest(self):
        raise NotImplementedError
    @abstractmethod
    def queryDb(self):
        raise NotImplementedError
    
class Mediator(MediatorIf):
    def __init__(self, database, client, server):
        self._database = database
        self._client = client
        self._server = server

        self._database.setMediator(self)
        self._client.setMediator(self)
        self._server.setMediator(self)

    def sendResponse(self, content):
        self._client.output(content)
    
    def makeRequest(self):
        self._server.process()
    
    def queryDb(self):
        return self._database.getData()

class Colleague():
    _mediator = None
    def setMediator(self, mediator):
        self._mediator = mediator

class Client(Colleague):
    def request(self):
        # in case of nullptr
        try:
            self._mediator.makeRequest()
        except AttributeError as e:
            print("Exception: {}".format(e))
            return
    
    def output(self, content):
        print(content)
    
class Database(Colleague):
    def getData(self):
        return 'World'

class Server(Colleague):
    def process(self):
        data = self._mediator.queryDb()
        self._mediator.sendResponse("Hello {}".format(data))


def execute_pattern():
    client = Client()
    # mediator super power!
    m = Mediator(Database(), client, Server())

    # 多米诺骨牌
    client.request()

if __name__ == '__main__':
    start = time.perf_counter()

    execute_pattern()
    print("Count: {} sec".format(time.perf_counter() - start))