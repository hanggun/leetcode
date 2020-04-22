# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        Using recursive to search the binary tree. When the preorder come in,
        the function will let the first node as the node and the first node
        after it as the left node and the first node bigger than it as the right
        node.
        :type preorder: List[int]
        :rtype: TreeNode
        """
        
        return self.helper(preorder, 0, len(preorder))
    
    def helper(self, preorder, start, end):
        
        if (start >= end):
            return None
        
        splitNum = start
        
        root = TreeNode(preorder[start])
        
        while splitNum < end and preorder[start] >= preorder[splitNum]:
            splitNum += 1
            
        root.left = self.helper(preorder, start + 1, splitNum)
        root.right = self.helper(preorder, splitNum, end)
        
        return root
    
def printInorder(root): 
    if root is None: 
        return 
    print(root.val)
    printInorder(root.left) 
    printInorder(root.right) 
    
solution = Solution()
node = solution.bstFromPreorder([8,5,1,7,10,12])
printInorder(node)