#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 12:02:34 2018

@author: Lin

Simple implementation of priority queue (high to low)

"""

class LSPriorityQBinaryHeap(object):
    def __init__(self, l):
        self.queue = l
        self.size = len(l) 
        for i in range(self.size):
            self.sink(i)
        
    def insert(self, data): 
        self.queue.append(data)
        self.size = self.size +1
        self.swim(self.size-1)
    
    def delete(self):
        maximum = self.queue[0] 
        self.queue[0] = self.queue[-1]
        self.queue.pop(-1)
        self.size = self.size - 1
        self.sink(0)        
        return maximum
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def great(self, i, j):
        return self.queue[i] > self.queue[j]
    
    def exchange(self, i, j):
        vi = self.queue[i]
        self.queue[i] = self.queue[j]
        self.queue[j] = vi
        
    def sink(self, k):
        while 2*k + 1 < self.size:
            j = 2*k + 1
            if j+1 < self.size and self.great(j+1, j):
                j = j + 1
            if not self.great(j, k):
                break
            self.exchange(j,k)
            k = j
    
    def swim(self, k):
        while k > 0 and self.great(k, int((k-1)/2) ):
            self.exchange(k, int((k-1)/2) )
            k = int((k-1)/2)    
            

if __name__ == '__main__':
    myQueue = LSPriorityQBinaryHeap([12, 1, 4, 7])
    myQueue.insert(17)
    print(myQueue.queue)
    while not myQueue.isEmpty():
        print(myQueue.delete())