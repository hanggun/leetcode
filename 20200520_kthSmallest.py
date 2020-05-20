# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        value = self.inorder(root)
        return value[k-1]
    
    def inorder(self, root):
        '''
        Using BST inorder method to get the value list

        Parameters
        ----------
        root : TYPE
            DESCRIPTION.

        Returns
        -------
        list
            DESCRIPTION.

        '''
        if root == None:
            return []
        
        left = self.inorder(root.left)
        val = [root.val]
        right = self.inorder(root.right)
        
        return left + val + right
    
    def printInorder(self, root): 
        if root is None: 
            return 
        print(root.val)
        self.printInorder(root.next)
        
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

        
nums = [5,3,6,2,4,None,None,1]
k = 3
length = len(nums)
root = insertLevelOrder(nums, None, 0, length)
solution = Solution()
print(solution.kthSmallest(root, k))