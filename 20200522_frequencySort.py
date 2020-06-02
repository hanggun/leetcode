class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s_dict = {}
        
        for i in s:
            s_dict[i] = s_dict.get(i, 0) + 1
            
        order_in_frequency = sorted(s_dict, key=lambda x: s_dict[x], reverse=True)
        
        char = ''
        for i in order_in_frequency:
            char = char + i * s_dict[i]
            
        return char
        
s = "tree"
solution = Solution()
print(solution.frequencySort(s))
