class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        
        digit = []
        
        for i in num:
            
            while(digit != [] and k != 0 and i < digit[-1]):
                digit.pop()
                k -= 1
                
            if digit != [] or i != '0':
                digit.append(i)
                
                
        while(digit != [] and k != 0):
            digit.pop()
            k -= 1
            
        if digit == []:
            return '0'
        
        return ''.join(digit)
    
num = "1432219"
k = 3
solution = Solution()
print(solution.removeKdigits(num, k))