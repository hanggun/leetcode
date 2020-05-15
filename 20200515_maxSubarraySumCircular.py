# -*- coding: utf-8 -*-
"""
Created on Fri May 15 15:27:23 2020

@author: Administrator
"""

class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        K = self.kadane(A)
        
        CircleLength = 0
        
        for i in range(len(A)):
            CircleLength += A[i]
            A[i] = -A[i]
            
        CircleLength += self.kadane(A)
        
        if K < CircleLength and CircleLength != 0:
            return CircleLength
        else:
            return K
        
        
    def kadane(self, A):
        '''
        Using max_ending_here to look for all positive contiguous segments of
        the array. Using max_so_far  to keep track of maximum sum contiguous
        segment among all positive segments
        '''
        
        from sys import maxsize
        max_ending_here = 0
        max_so_far = -maxsize
        
        for i in A:
            max_ending_here += i
                
            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
                
            if max_ending_here < 0:
                max_ending_here = 0
        
        return max_so_far
    
A = [5, -3, -2, -1, 4]
solution = Solution()
print(solution.maxSubarraySumCircular(A))
