"""
Proxy pattern for an bank acount.
"""

from abc import ABC, abstractmethod
import time
import logging

logger = logging.getLogger('pywrite')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

class BankAccount:
    @abstractmethod
    def deposit(self):
        raise NotImplementedError
    @abstractmethod
    def getBalance(self):
        raise NotImplementedError

class HeavyBankAccout(BankAccount):
    def __init__(self):
        "无持久化存储，单次进程账户交易模拟"
        self.RECORDED_BALANCE = 3000
        self.RECORDING = {}

    def commit(self, transanctions):
        logger.info("commit...")
        self.RECORDED_BALANCE += sum(transanctions.values())
        self.RECORDING.update(transanctions)
        time.sleep(5)

    def getBalance(self):
        """
        get real balance.
        Maybe read a large block of data from database and similar,
        This would be a very heavy operation.
        """
        time.sleep(5)
        return self.RECORDED_BALANCE
    
class BankAccountProxy(HeavyBankAccout):
    def __init__(self):
        super().__init__()
        self._balance = None
        self._transanctions = {}
        if self.RECORDING:
            # order id
            self._id = max(self.RECORDING.keys())
        else:
            self._id = 0

    def getBalance(self):
        "could do this parallelly"
        if not self._balance:
            self._balance = super().getBalance()
        return self._balance + sum(self._transanctions.values())
    
    def transanction(self, amount):
        self._id += 1
        self._transanctions[self._id] = amount
        logger.info(f"id: {self._id} transanction: {amount}")
    
    def cancel_transanction(self):
        logger.info(f"cancel transanction, id: {self._id}")
        self._transanctions.pop(self._id)
        self._id -= 1
    
    def finish(self):
        super().commit(self._transanctions)
        self._balance = None
        self._transanctions.clear()

if __name__ == '__main__':
    # could build a ATM command-line user client here
    #while input("What do you want? ") != 'q'
    anATM = BankAccountProxy()
    logger.info("Welcome to ATM!")

    anATM.transanction(+100)    # 存款
    anATM.transanction(-300)    # 取款
    logger.info(f"Get the current balance: {anATM.getBalance()}")
    anATM.transanction(3000)    # 转账入3000
    anATM.cancel_transanction() # cancel

    logger.info(f"Get the current balance: {anATM.getBalance()}")
    anATM.finish()
    logger.info(f"Get the current balance: {anATM.getBalance()}")
    logger.info(f"Get the current record: {anATM.RECORDING}")