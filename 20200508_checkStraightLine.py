class Solution(object):
    '''
    Compare the slope of each point
    '''
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        
        if len(coordinates) == 2:
            return True
        
        if (coordinates[1][0] - coordinates[0][0]) != 0:
            slope = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        else:
            slope = 0
        
        for i in range(1, len(coordinates)-1):
            if (coordinates[i+1][0] - coordinates[i][0]) != 0:
                slope_new = (coordinates[i+1][1] - coordinates[i][1]) / (coordinates[i+1][0] - coordinates[i][0])
            else:
                slope_new = 0
                
            if slope_new != slope:
                return False
            
        return True
    
coordinates = [[1,1],[2,2],[3,3],[4,4]]
solution = Solution()
print(solution.checkStraightLine(coordinates))