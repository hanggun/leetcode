class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        
        color = image[sr][sc]
        
        if newColor == color:
            return image
        
        image = self.helper(image, sr, sc, newColor, color)
        
        return image
    
    def helper(self, image, sr, sc, newColor, color):
        
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
            return image
        elif image[sr][sc] != color:
            return image
        
        image[sr][sc] = newColor

        image = self.helper(image, sr-1, sc, newColor, color)
        image = self.helper(image, sr+1, sc, newColor, color)
        image = self.helper(image, sr, sc-1, newColor, color)
        image = self.helper(image, sr, sc+1, newColor, color)
        
        return image
    
# image = [[1,1,1],[1,1,0],[1,0,1]]
image = [[0,0,0], [0,0,0]]
sr = 0
sc = 0
newColor = 2
solution = Solution()
print(solution.floodFill(image, sr, sc, newColor))