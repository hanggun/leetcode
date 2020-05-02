# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution(object):
    '''
    Here we use recursive from top level to the bottom level. In each level, we
    will check whether there is a node match the position of array. The only case
    that the arr is valid is that all the position is matched and no more nodes.
    '''
    def isValidSequence(self, root, arr):
        """
        :type root: TreeNode
        :type arr: List[int]
        :rtype: bool
        """
        
        length = len(arr)
        pos = 0
        
        return self.helper(root, length, pos, arr)
    
    def helper(self, root, length, pos, arr):
        '''
        Check from nodes to nodes

        Parameters
        ----------
        root : binary tree
            DESCRIPTION.
        length : int
            DESCRIPTION.
        pos : int
            DESCRIPTION.
        arr : list
            DESCRIPTION.

        Returns
        -------
        Logical

        '''
        
        if root == None or root.val == None:
            return False
        elif pos == length:
            return False
        elif root.val != arr[pos]:
            return False
        elif root.left == None and root.right == None and pos == length-1:
            return True
        
        return self.helper(root.left, length, pos+1, arr) or self.helper(root.right, length, pos+1, arr)
    
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
print(solution.isValidSequence(root, Tree))