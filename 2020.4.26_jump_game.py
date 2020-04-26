class Solution(object):
    '''
    Given the list and return whether you can get to the final index
    '''
    def canJump(self, nums):
        """
        I will use backwards method. Check whether the last good position can
        be reached. If all the last good position can be reached, then it can
        successfully get to the last index.
        e.g. [3,2,1,1,4]
        ------------------------------
        :type nums: List[int]
        :rtype: bool
        """
        
        lastGoodPosition = len(nums) - 1
        
        for i in range(lastGoodPosition, -1, -1):
             if(i + nums[i] >= lastGoodPosition):
                 lastGoodPosition = i
                 
        return lastGoodPosition == 0
    
# nums = [3,2,1,1,4]
nums = [3,2,1,0,4]
solution = Solution()
print(solution.canJump(nums))