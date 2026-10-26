# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2 or node1.val != node2.val:
                return False
            return isSameTree(node1.left, node2.left) and isSameTree(node1.right, node2.right)


        def dfs(root):

            if not root:
                return False
            
            if isSameTree(root, subRoot):
                return True
            
            # The Waiting Game: Ask the left and right branches to keep searching
            left_found = dfs(root.left)
            right_found = dfs(root.right)
            
            # Hand it up: If EITHER the left side OR the right side found it, return True
            return left_found or right_found
        
        return dfs(root)