class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #make a dictionary
        maxlength = 0
        occur = {}
        nums_sum = 0
        
        for i in range(len(nums)):
            
            nums_sum += -1 if nums[i] ==0 else 1
                
            if nums_sum == 0:
                maxlength = i + 1
                    
            if nums_sum in occur:
                maxlength = max(maxlength, i - occur[nums_sum])
            else:
                occur[nums_sum] = i
                
        return maxlength
    
nums = [0,0,1,1,0,1,0,0]
solution = Solution()
print(solution.findMaxLength(nums))