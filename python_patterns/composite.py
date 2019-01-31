"""
Composite pattern.
client use a group of objects and single object uniformly.
"""

from abc import ABC, abstractmethod

# interface 1
NOT_IMPLEMENTED = "You should implement this."

class Graphic(ABC):
    @abstractmethod
    def print(self):
        raise NotImplementedError(NOT_IMPLEMENTED)

class CompositeGraphic(Graphic):
    def __init__(self):
        self.graphics_ = []

    def print(self):
        for g in self.graphics_:
            g.print()
    
    def add(self, *g):
        "iterate *g to support add a collection of Graphic at once"
        for ele in g:
            self.graphics_.append(ele)
    
    def remove(self, g):
        self.graphics_.remove(g)

class Ellipse(Graphic):
    def __init__(self, name):
        self.name = name

    def print(self):
        print("Ellipse: ", self.name)

if __name__ == '__main__':
    ellipse1 = Ellipse("no.1")
    ellipse2 = Ellipse("no.2")
    ellipse3 = Ellipse("no.3")
    ellipse4 = Ellipse("no.4")

    ellipse_group1 = CompositeGraphic()
    ellipse_group2 = CompositeGraphic()
    graphic_collection = CompositeGraphic()

    ellipse_group1.add(ellipse1)
    ellipse_group2.add(ellipse2)
    ellipse_group2.add(ellipse3)
    graphic_collection.add(ellipse_group1, ellipse_group2, ellipse4)
    graphic_collection.print()