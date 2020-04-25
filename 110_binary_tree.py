# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    '''
    This function is used to check a binary tree in which the left and right 
    subtrees of every node differ in height by no more than 1.
    '''
        
    def isBalanced(self, root):
        '''
        

        Parameters
        ----------
        root : baniry tree's root
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        
        return self.maxDepth(root) != None
    
    def maxDepth(self, root):
        '''
        Calculate the maximum Depth of left tree and right tree

        Parameters
        ----------
        root : TYPE
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        if root == None or root.val == None:
            return 0
        
        left_maxDepth = self.maxDepth(root.left)
        right_maxDepth = self.maxDepth(root.right)
        
        #left is 0 or 2 and right is 2 or 0
        if left_maxDepth == None or right_maxDepth == None:
            return None
        
        if abs(left_maxDepth - right_maxDepth) > 1:
            return None
        
        return max(left_maxDepth, right_maxDepth) + 1


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

# Tree = [3,9,20,None,None,15,7]
Tree = [1,2,2,3,3,None,None,4,4]
length = len(Tree)
root = insertLevelOrder(Tree, None, 0, length)
solution = Solution()
print(solution.isBalanced(root))