import numpy as np

class Solution(object):
    def findJudge(self, N, trust):
        """
        Here I will use two dictionary to find the judge. The judge has two
        requirement.
        1. He trust nobody
        2. He is trusted by everyone
        So the judge will not appear in the trust dictionary and The judge in
        the trusted dictionary will be n-1
        
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        
        if trust == []:
            return 1
        
        trust_dict = {}
        trusted_dict = {}
        
        for i in range(len(trust)):
            trust_dict[trust[i][0]] = trust_dict.get(trust[i][0], 0) + 1
            
        for i in range(len(trust)):
            trusted_dict[trust[i][1]] = trusted_dict.get(trust[i][1], 0) + 1
            
        total_person = list(range(1, N+1))
        judge_candidate = np.setdiff1d(total_person, list(trust_dict.keys()))
        
        if len(judge_candidate) == 0:
            return -1
        
        for i in judge_candidate:
            if i in trusted_dict.keys() and trusted_dict[i] == N-1:
                return i
            
        return -1
    
N = 4
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
solution = Solution()
print(solution.findJudge(N, trust))