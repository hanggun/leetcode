class Solution(object):
    '''
    This function, we will implement right shift to the number and plus the 
    1 with left shift if the binary place is not 1.
    '''
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        i = 0
        Result = 0
        
        while num > 0:
            
            if num & 1 == 0:
                Result += 1 << i
                
            i += 1
            num = num >> 1
                
                
        return Result
    
solution = Solution()
print(solution.findComplement(5))