# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import sys

class Solution(object):
    '''
    This function will start from the left bottom node. Compare the stright way
    up and the maximum sum of leaf leaf and right leaf. The result will save the
    maximum path it ever appears.
    '''
    def __init__(self):
        self.result = -sys.maxsize
        
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.maxPathSum_Util(root)
        
        return self.result
    
    def maxPathSum_Util(self, root):
        
        if root == None or root.val == None:
            return 0
        
        left = self.maxPathSum_Util(root.left)
        right = self.maxPathSum_Util(root.right)

        max_straight = max(max(left, right) + root.val, root.val) 
        max_caseVal = max(max_straight, left+right+root.val)
        
        self.result = max(self.result, max_caseVal)
        
        return max_straight
    
    
# Function to insert nodes in level order  
def insertLevelOrder(arr, root, i, n): 
    '''
    Build a binary tree from list

    Parameters
    ----------
    arr : Binary tree list
        DESCRIPTION.
    root : TYPE
        DESCRIPTION.
    i : int
        place of the root
    n : int
        length of tree

    Returns
    -------
    root : current binary tree
        DESCRIPTION.

    '''
    # Base case for recursion  
    if i < n:
        temp = TreeNode(arr[i])
        root = temp
        
        #insert left leaf
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)
        
        #insert right leaf
        root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)
        
    return root

Tree = [1,2,2,3,3,None,None,4,4]
length = len(Tree)
root = insertLevelOrder(Tree, None, 0, length)
solution = Solution()
print(solution.maxPathSum(root))