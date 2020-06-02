# -*- coding: utf-8 -*-
"""
Created on Mon May 18 15:42:10 2020

@author: Administrator
"""

from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        num_s1 = len(s1)
        num_s2 = len(s2)
        
        dict_s1 = Counter(s1)
        dict_s2 =Counter()
        
        for i in range(num_s2):
            dict_s2[s2[i]] += 1
            if i >= num_s1:
                if dict_s2[s2[i-num_s1]] == 1:
                    del dict_s2[s2[i-num_s1]]
                else:
                    dict_s2[s2[i-num_s1]] -= 1
                
            if dict_s2 == dict_s1:
                return True
            
        return False
        
        
        
s1 = 'adc'
s2 = 'dcda'

solution = Solution()
print(solution.checkInclusion(s1,s2))