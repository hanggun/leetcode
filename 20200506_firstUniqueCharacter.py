class Solution(object):
    '''
    Here, I will use dictionary to record every letter's occurance. And use a 
    list to find out the first unique character
    '''
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        stringDict = {}
        strList = list(s)
        num = 0
        for i in s:
            stringDict[i] = stringDict.get(i,0) + 1
            
        while strList != [] and stringDict[strList[0]] > 1:
            num += 1
            strList.pop(0)
            
        if strList == []:
            return -1
        
        return num
    
s = 'leetcode'
solution = Solution()
print(solution.firstUniqChar(s))