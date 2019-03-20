"""
Facade
Law of Demeter
best facade has no new or constructors
https://en.wikipedia.org/wiki/Facade_pattern
"""

from abc import ABC, abstractmethod
import unittest
#import pdb
#import logging

class CPU:
    _header = "CPU: "
    def freeze(self):
        print(self._header + "freezing...")
    def jump(self, position):
        print(f"{self._header} jumping to {position}...")
    def execute(self):
        print(f"{self._header} executing...")

class HardDrive:
    def read(self, lba, size) -> str:
        return f"Hard Drive: reading {size} from {lba}"

class Memory:
    def load(self, position, data):
        print(f"Loading from {position}, data - {data}.")

class Facade(ABC):
    "get a boot addresss"
    BOOT_ADDR = '0x00000036'
    JUMP_ADDR = '0x00001000'
    def __init__(self, cpu, hd, mem):
        self._cpu = cpu
        self._hd = hd
        self._mem = mem

    def turnOn(self):
        "computer start"
        self._cpu.freeze()
        self._mem.load(self.BOOT_ADDR, self._hd.read('Boot Image file', '16KB'))
        self._cpu.jump(self.JUMP_ADDR)
        self._cpu.execute()

    def turnOff(self):
        pass


if __name__ == '__main__':
    c = CPU()
    h = HardDrive()
    m = Memory()

    f = Facade(c, h, m)
    f.turnOn()