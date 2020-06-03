class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        #建立动态规划表
        num1 = len(word1)
        num2 = len(word2)
        dp = [[0 for i in range(num1+1)] for j in range(num2+1)]
        
        for i in range(num2+1):
            for j in range(num1+1):
                
                #如果word1的长度为空，那么要变成word2则需要进行不断的插入，插入的
                #长度等于word2的长度
                if i == 0:
                    dp[i][j] = j
                #如果word2的长度为空，那么要变成word1则需要不断的进行移除，移除的
                #长度等于word1的长度
                elif j == 0:
                    dp[i][j] = i
                #如果当前的word1和word2的最后一个字母相同，则不需要进行处理，并跳
                #至dp[i-1][j-1]
                elif word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                #如果当前的word1和word2的最后一个字母不相同，则处理的次数等于插入
                #或者移除或者替换中最小的操作+1
                elif word1[j-1] != word2[i-1]:
                    dp[i][j] = 1 + min(dp[i-1][j],#插入
                                       dp[i-1][j-1],#替换
                                       dp[i][j-1])#移除
                    
        return dp[i][j]
word1 = 'Sunday'
word2 = 'Saturday'
solution = Solution()
print(solution.minDistance(word1, word2))