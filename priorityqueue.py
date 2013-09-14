"""
SQLite based Persistent Priority Queue
FIFO Queue and LIFO Stack subclasses
"""

import sqlite3
from time import time

class PriorityQueue(object):
    """
    Persistent PriorityQueue 
    A higher number indicates higher priority
    """
    def __init__(self, queue_name):
        """
        Initialize the database file and create tables
        """
        self.__conn = sqlite3.connect('%s' % queue_name)
        self.__cursor = self.__conn.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS
        priority_queue(
            priority REAL PRIMARY KEY, 
            item TEXT
        )
        """
        self.__cursor.execute(sql)
        self.__conn.commit()

    def push(self, priority, item):
        """
        Push item with to priority into the PriorityQueue
        """
        sql = """
        INSERT INTO 
        priority_queue
        VALUES(?, ?)
        """
        self.__cursor.execute(sql, (priority, item))
        self.__conn.commit()

        return item

    def pop(self):
        """
        Pop the item with the highest priority
        Retrieves and deletes the row
        """
        sql = """
        SELECT priority, item  
        FROM priority_queue
        ORDER BY priority DESC 
        LIMIT 1
        """
        self.__cursor.execute(sql)
        priority, item = self.__cursor.fetchone()

        sql = """
        DELETE  
        FROM priority_queue
        WHERE priority = ?
        """
        self.__cursor.execute(sql, (priority,))
        self.__conn.commit()

        return item

    def is_empty(self):
        """
        Returns a boolean indicating if queue is empty
        """
        sql = """
        SELECT COUNT(*)
        FROM priority_queue
        """
        self.__cursor.execute(sql)
        count = self.__cursor.fetchone()[0]
        
        if count == 0: return True
        else: return False

class Queue(PriorityQueue):
    """
    A FIFO Queue
    """
    def push(self, item):
        priority = -time()
        return super(Queue, self).push(priority, item)

class Stack(PriorityQueue):
    """
    A LIFO Stack
    """
    def push(self, item):
        priority = time()
        return super(Stack, self).push(priority, item)
