class Solution(object):
    def intervalIntersection(self, A, B):
        """
        If the interval intersection exist, then the start of intersection 
        start is the maximum start value of two interval and the intersection
        end is the minimum end value of two interval.
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        
        a = 0
        b = 0
        interval = []
        
        while a < len(A) and b < len(B):
            
            interval_start, interval_end = max(A[a][0], B[b][0]), min(A[a][1], B[b][1])
            
            if interval_start <= interval_end:
                interval.append([interval_start, interval_end])
                
            if A[a][1] < B[b][1]:
                a += 1
            else:
                b += 1
            
        return interval
    
A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
solution = Solution()
print(solution.intervalIntersection(A,B))