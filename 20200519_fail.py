# -*- coding: utf-8 -*-
"""
Created on Tue May 19 13:00:35 2020

@author: Administrator
"""

from sys import maxsize

class TreeNone(object):
    
    def __init__(self, x=None):
        self.val = x
        self.next = None
        
class StockSpanner(object):

    def __init__(self):
        self.root = TreeNone(maxsize)
        self.value = 1
        self.compare = 1

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        #set start value to 1
        self.value = 1
        self.compare = True
        parent = self.root
        
        self.helper(parent, price)
        
        return self.value
        
    def helper(self, root, price):
        '''
        This function aims to use recursion. Come to the leaf and then compare
        backwards.
        '''
        
        if root.next == None:
            
            root.next = TreeNone(price)
            
            if root.val <= price:
                if self.compare >= 1:
                    self.value += 1
            else:
                self.compare -= 1
                
            return
        
        self.helper(root.next, price)
        
        if root.val <= price:
            if self.compare >= 1:
                self.value += 1
        else:
            self.compare -= 1
        
S = StockSpanner()
print(S.next(100))
print(S.next(80))
print(S.next(60))
print(S.next(70))
print(S.next(60))
print(S.next(75))
print(S.next(85))