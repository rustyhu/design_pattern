"""composite pattern."""

# how to make base class abstract
# (derives must implement specific abstract method) in python? 
from abc import ABC
from abc import abstractmethod

# interface 1
class WebPage(ABC):
    @abstractmethod
    def getContent(self):
        pass

class About(WebPage):
    theme_ = None
    def __init__(self, t):
        self.theme_ = t

    def getContent(self):
        return  "About page in " + self.theme_.getColor()

class Careers(WebPage):
    theme_ = None
    def __init__(self, t):
        self.theme_ = t

    def getContent(self):
        return  "Careers page in " + self.theme_.getColor()

# interface 2
class theme(ABC):
    @abstractmethod
    def getColor(self):
        pass

class black(theme):
    def getColor(self):
        return "black wallpaper theme!"

class blue(theme):
    def getColor(self):
        return "blue wallpaper theme!"

class aque(theme):
    def getColor(self):
        return "gray wallpaper theme!"

if __name__ == '__main__':
    a = About(black())
    print(a.getContent())

    b = Careers(aque())
    print(b.getContent())
