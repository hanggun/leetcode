# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    '''
    In this function, I will find the parent of x and y and the height of x and
    y. If x and y have different parent and their height is the same. Then they
    are cousins
    '''
    def __init__(self):
        
        self.parent = 0
        self.xParent = 0
        self.yParent = 0
        
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        
        #If one of the x or y equal to root, then they will never be cousins
        if root.val == x or root.val == y:
            return False
        
        xHeight = self.findHeight(root, x, 0)
        self.xParent = self.parent
        yHeight = self.findHeight(root, y, 0)
        self.yParent = self.parent
        
        if self.xParent != self.yParent and xHeight == yHeight:
            return True
        else:
            return False
        
    def findHeight(self, root, x, height):
        
        if root == None or root.val == None:
            return 0
        
        if root.val == x:
            return height
        
        self.parent = root.val
        left = self.findHeight(root.left, x, height+1)
        if left:
            return left
        
        self.parent = root.val
        right = self.findHeight(root.right, x, height+1)
        return right