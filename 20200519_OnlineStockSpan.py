# -*- coding: utf-8 -*-
"""
Created on Tue May 19 13:00:35 2020

@author: Administrator
"""
   
class StockSpanner(object):

    def __init__(self):
        
        #set a global stack
        self.price_stack = []

    def next(self, price):
        """
        Use stack to compare value from back to begining
        :type price: int
        :rtype: int
        """
        
        span = 1
        
        #whenever a price come in, compare it to the last one
        while self.price_stack and self.price_stack[-1][0] <= price:
            span = span + self.price_stack.pop()[1]
        
        self.price_stack.append([price,span])
            
        return span
        
        
S = StockSpanner()
print(S.next(100))
print(S.next(80))
print(S.next(60))
print(S.next(70))
print(S.next(60))
print(S.next(75))
print(S.next(85))