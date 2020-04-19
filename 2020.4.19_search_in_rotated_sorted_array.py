class Solution(object):
    '''
    This function uses binary search to find the index of target. For the 
    ordinary step, it needs n step to find the target. Binary Search only 
    needs log(n) step. The nums is a sorted rotated array.
    '''
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target not in nums:
            return -1
        
        left = 0
        right = len(nums)-1
        
        
        while(left <= right):
            
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] < nums[right]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
            else:
                if target >= nums[left] and target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
                    
solution = Solution()
print(solution.search([4,5,6,7,0,1,2], 0))   
print(solution.search([1], 1))  
print(solution.search([1,3], 3))  