"""
Dependency injection
reference: https://stackoverflow.com/questions/130794/what-is-dependency-injection
"""

import unittest
#import pdb
#import logging

class DatabaseConfiguration:
    def __init__(self, host, port, username, password):
        self._host = host
        self._port = port
        self._username = username  
        self._password = password 

    @property
    def host(self):
        return self._host
    @property
    def port(self):
        return self._port
    @property
    def username(self):
        return self._username
    @property
    def password(self):
        return self._password
    
class DatabaseConnection:
    def __init__(self, config: DatabaseConfiguration):
        "Dependency 'config' is injected via this constructor argument."
        self._configuration = config

    def getDsn(self):
        return '%s:%s@%s:%d' % (
            self._configuration.username,
            self._configuration.password,
            self._configuration.host,
            self._configuration.port)

if __name__ == '__main__':
    # An object should not be responsible for the creation of its dependencies.
    connection = DatabaseConnection(
        DatabaseConfiguration('localhost', 3306, 'domnikl', '1234'))
    print(connection.getDsn())
