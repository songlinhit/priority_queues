#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 12:02:34 2018

@author: Lin

Simple implementation of priority queue (low to high)

"""

class LSPriorityQSimple(object):
    def __init__(self, l):
        self.queue = l
        
    def insert(self, data): # complexity of insert is O(0)
        self.queue.append(data)
    
    def delete(self):
        maximum = max(self.queue) # complexity of max is O(n) linear
        self.queue.remove(maximum)
        return maximum
    
    def isEmpty(self):
        return len(self.queue) == 0
            

if __name__ == '__main__':
    myQueue = LSPriorityQSimple([12, 1, 4, 7])
    myQueue.insert(17)
    print(myQueue.queue)
    while not myQueue.isEmpty():
        print(myQueue.delete())