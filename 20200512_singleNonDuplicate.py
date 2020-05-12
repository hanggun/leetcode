class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        Using bisection method to find the non-duplicate element. If the element
        is not equal to left one and right one, then it is a unique one. If the
        pair start from even number, then search to right. If the pair start from
        odd, then search to left. Until we find the unique element
        :type nums: List[int]
        :rtype: int
        """
        
        high = len(nums) - 1
        low = 0
        
        if high == 0:
            return nums[0]
        elif nums[0] != nums[1]:
            return nums[0]
        elif nums[high] != nums[high-1]:
            return nums[high]
        
        while low <= high:
            
            mid = (low + high) // 2
            
            if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
                return nums[mid]
            
            if ((mid % 2 == 0 and nums[mid] == nums[mid+1]) or
                (mid % 2 == 1 and nums[mid] == nums[mid-1])):
                low = mid + 1
            else:
                high = mid - 1
                
                
nums = [3,3,7,7,10,11,11]
solution = Solution()
print(solution.singleNonDuplicate(nums))