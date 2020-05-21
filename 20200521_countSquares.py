# -*- coding: utf-8 -*-
"""
Created on Thu May 21 17:43:18 2020

@author: Administrator
"""

import numpy as np

class Solution(object):
    def countSquares(self, matrix):
        """
        Using dynamic programming. First pad 0s to the original matrix. 
        Second, compare the current value to top, left and topleft value:
        1 if there is 0
        a[i-1][j-1] + 1 otherwise
        using count to sum all the value
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        #create a padding matrix
        rows = len(matrix)
        cols = len(matrix[0])
        matrix_pad = np.zeros([rows+1, cols+1], dtype=int)
        
        #count the submatrices
        count = 0
        
        #compare to the original matrix
        for i in range(rows):
            for j in range(cols):
                
                if matrix[i][j] == 0:
                    matrix_pad[i+1][j+1] = 0
                else:
                    
                    if matrix_pad[i][j] == 0 or matrix_pad[i][j+1] == 0 \
                        or matrix_pad[i+1][j] == 0:
                        matrix_pad[i+1][j+1] = 1
                        count += matrix_pad[i+1][j+1]
                    else:
                        matrix_pad[i+1][j+1] = min(matrix_pad[i][j], matrix_pad[i][j+1],
                                                   matrix_pad[i+1][j]) + 1
                        count += matrix_pad[i+1][j+1]
                        
        return count
    
matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
matrix = [
  [0,1,1],
  [1,1,1],
  [0,1,1]
]
matrix = [
  [1,1,1],
  [1,1,1],
  [1,1,1]
]
solution = Solution()
print(solution.countSquares(matrix))
