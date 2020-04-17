# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 22:53:30 2020

@author: Administrator
"""

import numpy as np

class Solution(object):
    def checkValidString(self, s):
        """
        This function use stack method to do the validation. For each open bracket
        ( and star *, the stack will add it directly. when close symbol ) come, it
        will check whether there is open bracket exist, if no, add the close bracket,
        pop the closest open bracket, otherwise. Then check the combination of *) and
        (*. Finally check  the single *.
        -------------
        :type s: str
        :rtype: bool
        """
        
        open_bar = ['(', '*']
        stack = []
        for i in s:
           if i in open_bar:
               stack.append(i)
           else:
               if '(' in stack:
                   j = -1
                   while stack[j] == '*':
                       j -= 1
                   stack.pop(j)
               else:
                   stack.append(i)
                   
        String = ''.join(stack)
            
        while '*)' in String or '(*' in String:
            String = String.replace('*)', '').replace('(*', '')
            
        while '*' in String:
            String = String.replace('*', '')
            
        if String == '':
            return True
        else:
            return False
        
class Solution1(object):
    def checkValidString(self, s):
        if not s: return True
        A = list(s)
        self.ans = False

        def solve(i):
            if i == len(A):
                self.ans |= valid()
            elif A[i] == '*':
                for c in '() ':
                    A[i] = c
                    solve(i+1)
                    if self.ans: return
                A[i] = '*'
            else:
                solve(i+1)

        def valid():
            bal = 0
            for x in A:
                if x == '(': bal += 1
                if x == ')': bal -= 1
                if bal < 0: break
            return bal == 0

        solve(0)
        return self.ans
    
def posibility():
    '''
    Test the Parenthesis validation function
    '''
    solution = Solution()
    print(solution.checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*"))
    print(solution.checkValidString("(*()"))
    print(solution.checkValidString("(*)"))
    print(solution.checkValidString("(*))"))
    print(solution.checkValidString('((*)'))
    print(solution.checkValidString("((()))()(())(*()()())**(())()()()()((*()*))((*()*)"))
    
def posibility1():
        '''
    Test the Parenthesis validation function1
    '''
    solution = Solution1()
    print(solution.checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*"))
    print(solution.checkValidString("(*()"))
    print(solution.checkValidString("(*)"))
    print(solution.checkValidString("(*))"))
    print(solution.checkValidString('((*)'))
    print(solution.checkValidString("((()))()(())(*()()())**(())()()()()((*()*))((*()*)"))
    
posibility1()
    
