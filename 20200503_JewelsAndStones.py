class Solution(object):
    '''
    Use dictionary to find out the number of jeweries you have in stones
    '''
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        
        JeweryDict = {}
        count = 0
        for i in J:
            JeweryDict[i] = JeweryDict.get(i, 0) + 1
            
        for i in S:
            if i in JeweryDict.keys():
                count += 1
                
        return count
        

J = "aA"
S = "aAAbbbb"
solution = Solution()
print(solution.numJewelsInStones(J,S))