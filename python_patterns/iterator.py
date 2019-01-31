"""
iterator
"""

from abc import ABC, abstractmethod
# performance test
import timeit
#import logging

class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author
    
    def getAuthor(self):
        return self._author
    
    def getTitle(self):
        return self._title
    
class BookList:
    def __init__(self):
        self._books = []
        self._index = 0

    def __iter__(self):
        "implement iterator"
        return iter(self._books)

    def addBook(self, book):
        self._books.append(book)
        return self

    def rmBook(self, bookToRm):
        for b in self._books:
            if b.getTitle() == bookToRm.getTitle():
                self._books.remove(b)
        return self
    

if __name__ == '__main__':
    a = BookList()\
    .addBook(Book('Wanderer', 'Liu'))\
    .addBook(Book('The story of 1900', 'Ada'))\
    .addBook(Book('Invalid', 'whoever'))\
    .rmBook(Book('Invalid', 'whoever'))

    for b in a:
        print(b.getAuthor())