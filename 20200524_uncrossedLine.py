class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        Using dynamic programming.
        1. make a len(A)+1 by len(B)+1 matrix which is pading for DP
        2. if match, then the value is equal to diagonal value + 1
        3. if not match, then the value is the maximum row or column
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        
        #Pading
        dp = [[0 for i in range(len(B)+1)] for j in range(len(A)+1)]
        
        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                if B[j-1] == A[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[i][j]
    
A = [2,5,1,2,5]
B = [10,5,2,1,5,2]
solution = Solution()
print(solution.maxUncrossedLines(A, B))