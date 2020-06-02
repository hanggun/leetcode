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
        '''
        This function is provided by leetcode, it used recursive method to validate
        the parenthesis. It searches all the star * in the string and replace it with
        '(', ')' and ' '. Calculate the number of '(' and ')'. If any of the senarios
        have matched, the string is validated.
        '''
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
    
class Solution2(object):
    '''
    Dynamic Programming, But can not understand
    
    Let dp[i][j] be true if and only if the interval s[i], s[i+1], ..., s[j] can 
    be made valid. Then dp[i][j] is true only if:

    s[i] is '*', and the interval s[i+1], s[i+2], ..., s[j] can be made valid;
    
    or, s[i] can be made to be '(', and there is some k in [i+1, j] such that 
    s[k] can be made to be ')', plus the two intervals cut by s[k] (s[i+1: k] 
    and s[k+1: j+1]) can be made valid;
    '''
    def checkValidString(self, s):
        if not s: return True
        LEFTY, RIGHTY = '(*', ')*'

        n = len(s)
        dp = [[False] * n for _ in s]
        for i in range(n):
            if s[i] == '*':
                dp[i][i] = True
            if i < n-1 and s[i] in LEFTY and s[i+1] in RIGHTY:
                dp[i][i+1] = True

        for size in range(2, n):
            for i in range(n - size):
                if s[i] == '*' and dp[i+1][i+size]:
                    dp[i][i+size] = True
                elif s[i] in LEFTY:
                    for k in range(i+1, i+size+1):
                        if (s[k] in RIGHTY and
                                (k == i+1 or dp[i+1][k-1]) and
                                (k == i+size or dp[k+1][i+size])):
                            dp[i][i+size] = True

        return dp[0][-1]
    
class Solution3(object):
    '''
    Greedy Search
    
    
    '''
    def checkValidString(self, s):
        lo = hi = 0
        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            if hi < 0: break
            lo = max(lo, 0)

        return lo == 0
    
def possibility():
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
    
def possibility1():
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
    
def possibility2():
    '''
    Test the Parenthesis validation function1
    '''
    solution = Solution2()
    print(solution.checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*"))
    print(solution.checkValidString("(*()"))
    print(solution.checkValidString("(*)"))
    print(solution.checkValidString("(*))"))
    print(solution.checkValidString('((*)'))
    print(solution.checkValidString("((()))()(())(*()()())**(())()()()()((*()*))((*()*)")) 
    
def possibility3():
    '''
    Test the Parenthesis validation function1
    '''
    solution = Solution3()
    print(solution.checkValidString(")("))
#    print(solution.checkValidString("(*)"))
#    print(solution.checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*"))
#    print(solution.checkValidString("(*()"))
#    print(solution.checkValidString("(*))"))
#    print(solution.checkValidString('((*)'))
#    print(solution.checkValidString("((()))()(())(*()()())**(())()()()()((*()*))((*()*)")) 
    
possibility3()
