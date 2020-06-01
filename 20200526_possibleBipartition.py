class Solution(object):
    
    def __init__(self):
        #set color vector
        self.color = 0
        
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        
        #set color vector
        self.color = [-1 for i in range(N+1)]
        
        #set adjacent vector
        adj = [[] for i in range(N+1)]
        
        #construct adjacent vector
        for i in range(len(dislikes)):
            adj[dislikes[i][0]].append(dislikes[i][1])
            adj[dislikes[i][1]].append(dislikes[i][0])
            
        
        #check whether it is a bipartile graph
        for i in range(1, N+1):
            if self.color[i] == -1:
                if (not self.isBipartile(adj, N, i)):
                    return False
        return True

    def isBipartile(self, adj, N, node):
        
        #set a queue
        q = []
        q.append(node)
        self.color[node] = 1
        
        #Process current graph component using BFS
        while(q != []):
            curr = q[-1]
            q.pop()
            for ele in adj[curr]:
                if self.color[ele] == self.color[curr]: #odd cycle
                    return False
                if self.color[ele] == -1:
                    self.color[ele] = 1-self.color[curr]
                    q.append(ele)
                    
        return True
        
N = 4
dislikes = [[1,2],[1,3],[2,4]]
solution = Solution()
print(solution.possibleBipartition(N, dislikes))