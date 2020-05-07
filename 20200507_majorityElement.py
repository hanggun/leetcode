class Solution(object):
    '''
    This function is going to find the element which appears more than n/2 times.
    the array is always non-empty and the majority element is always in the list
    '''
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums_dict = {}
        for i in nums:
            nums_dict[i] = nums_dict.get(i, 0) + 1
            
        biggest_number = max(nums_dict.values())
        for key, value in nums_dict.items():
            if value == biggest_number:
                return key
            
            
nums = [2,2,1,1,1,2,2]
solution = Solution()
print(solution.majorityElement(nums))