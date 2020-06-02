class Solution(object):
    '''
    Here I will use bisection method to find whether the number is perfect
    squared
    '''
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        low = 0
        high = num
        
        while low <= high:
            mid = (low + high) // 2
            
            if mid ** 2 > num:
                high = mid - 1
            elif mid ** 2 < num:
                low = mid + 1
            else:
                return True
            
        return False
    
solution = Solution()
print(solution.isPerfectSquare(16))
                