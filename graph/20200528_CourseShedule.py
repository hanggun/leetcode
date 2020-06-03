class Solution(object):
    
    def __init__(self):
        self.adj = 0
        self.visitor = 0
        
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        #建立相邻矩阵（直线图）
        self.adj = [[] for i in range(numCourses)]
        for i in range(len(prerequisites)):
            self.adj[prerequisites[i][0]].append(prerequisites[i][1])
            
        #建立探索向量, 0意味着未探索过
        self.visitor = [0 for i in range(numCourses)]
        
        #从第一个节点开始依次向后寻找，如果该节点未被探索过，则使用BFS进行探索是否
        #有圆圈结构，如果有圆圈结构，则不能完成所有课程
        for i in range(numCourses):
            if self.visitor[i] == 0:
                if self.isCyclic(i):
                    return False
        
        return True
                
    def isCyclic(self, curr):
        
        #一开始进来的节点是为0，如果再次进入节点时，标记为正在处理，则代表此处有死循环
        if self.visitor[curr] == 2:
            return True
        
        #首先标记为2意为正在处理
        self.visitor[curr] = 2
        
        #从该节点开始，对其相邻节点进行处理，如果相邻节点没有被处理完，则跳到相邻
        #节点对相邻节点进行处理
        for i in self.adj[curr]:
            if self.visitor[i] != 1:
                if self.isCyclic(i):
                    return True
       
        #若没有可处理的节点了，则将该节点标记为1意为已处理完，并返回至上一节点
        self.visitor[curr] = 1
        
        return False
    
numCourses = 2
prerequisites = [[1,0],[0,1]]
solution = Solution()
print(solution.canFinish(numCourses, prerequisites))