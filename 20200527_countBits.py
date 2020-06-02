class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        #create a memory vector to record the bit's count fo each number
        mem = [0 for i in range(num+1)]
        
        #using the previous solution, for even number, the count bits is
        #equal to the number//2, for odd number, the count bits is equal
        #to the number
        for i in range(1, num+1):
            mem[i] = mem[i//2] + i % 2
            
        return mem
    
num = 8
solution = Solution()
print(solution.countBits(num))