from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        I will check every substring in s from first index to n-len(p). Using 
        dictionary and compare whether all the characters match.
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        #set a empty list to store index with anagrams
        good_index = []
        
        num_s = len(s)
        num_p = len(p)
        
        if num_s < num_p:
            return []
        
        #create two dictionary
        dict_s = Counter()
        dict_p = Counter(p)
            
        for i in range(num_s):
            #record the character's occurance in this place
            dict_s[s[i]] += 1
            
            if i > num_p-1:
                if dict_s[s[i-num_p]] == 1:
                    del dict_s[s[i-num_p]]
                else:
                    dict_s[s[i-num_p]] -= 1
                
            if dict_s == dict_p:
                good_index.append(i-num_p+1)
                
        return good_index
    
solution = Solution()
s = "abab"
p = "ab"
print(solution.findAnagrams(s,p))

