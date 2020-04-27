import numpy as np

class Solution(object):
    '''
    This function uses dynamic programming to find the longest common string
    between two strings. Using dynamic programming, the (i,j) position is equal
    to the largest number of (i-1,j) & (i, j-1) or (i-1, j-1) place.
    '''
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
        lengthText1 = len(text1)
        lengthText2 = len(text2)
        
        DP = np.zeros([lengthText1+1, lengthText2+1], dtype=int)
        
        #Dynamic programming
        for i in range(1, lengthText1+1):
            for j in range(1, lengthText2+1):
                if text1[i-1] == text2[j-1]:
                    DP[i][j] = DP[i-1][j-1] + 1
                else:
                    DP[i][j] = max(DP[i-1][j], DP[i][j-1])
                    
        return DP[lengthText1, lengthText2]
    
text1 = 'abcde'
text2 = 'ace'
solution = Solution()
print(solution.longestCommonSubsequence(text1, text2))