import numpy as np

class Solution(object):
    '''
    Thik function used dynamic programming to find the maximal sub matrix with
    all zero. The intuition is that if the square has all 1. Then the length of
    square matrix of three direction ----vertival, horizontal, diagonal, are the
    same.
    '''
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []:
            return 0
        
        ver = len(matrix[0])
        hor = len(matrix)
        
        Matrix = np.array(matrix, dtype=int)
        DP = np.zeros([hor+1, ver+1], dtype=int)
        
        for i in range(1, hor+1):
            for j in range(1, ver+1):
                if Matrix[i-1,j-1] == 1:
                    DP[i,j] = min(DP[i-1,j-1], DP[i, j-1], DP[i-1, j]) +1
                else:
                    DP[i,j] = 0
                
        return np.max(DP) ** 2
    
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"]]
solution = Solution()
print(solution.maximalSquare(matrix))