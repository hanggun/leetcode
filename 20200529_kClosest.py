class Solution(object):
    def kClosest(self, points, K):
        """
        使用欧几里得距离获得离原点最近的k个点，并返回那k个点
        想法：
        计算出所有点距离原点的距离，排序，然后输出对应的k个点
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        
        #计算所有点的距离
        distance = []
        for i in range(len(points)):
            distance.append((points[i][0])**2 + (points[i][1])**2)
            
        #从小到大排序列表的序号
        index = sorted(range(len(distance)), key=lambda k: distance[k])
        
        closest = []
        for i in range(K):
            closest.append(points[index[i]])
            
        return closest
points = [[3,3],[5,-1],[-2,4]]
K = 2
solution = Solution()
print(solution.kClosest(points, K))