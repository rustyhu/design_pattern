"""decorator pattern."""

# how to make base class abstract
# (derives must implement specific abstract method) in python? 
from abc import ABC
from abc import abstractmethod

# interface
class Booking(ABC):
    @abstractmethod
    def calculatePrice(self):
        raise NotImplementedError
    @abstractmethod
    def getDescription(self):
        raise NotImplementedError

# basic Booking
class SingleRoom(Booking):
    def calculatePrice(self):
        return 20
    def getDescription(self):
        return 'single room'

class DoubleRoom(Booking):
    def calculatePrice(self):
        return 40
    def getDescription(self):
        return 'double room'
        
    
# decorator base
class BookingDecorator(Booking):
    def __init__(self, origin: Booking, description, extrefee):
        self._origin = origin
        self._description = description
        self._extraFee = extrefee

    def calculatePrice(self):
        return self._origin.calculatePrice() + self._extraFee
    def getDescription(self):
        return self._origin.getDescription() + self._description

# decorators
class WIFI(BookingDecorator):
    def __init__(self, origin):
        BookingDecorator.__init__(self, origin, " with WIFI", 10)

class ExtraBed(BookingDecorator):
    def __init__(self, origin):
        BookingDecorator.__init__(self, origin, " with extra bed", 30)


if __name__ == '__main__':
    order1 = DoubleRoom()
    print("order 1: {}, Price: {}".format(order1.getDescription(), order1.calculatePrice()))
    order2 = WIFI(ExtraBed(SingleRoom()))
    print("order 2: {}, Price: {}".format(order2.getDescription(), order2.calculatePrice()))