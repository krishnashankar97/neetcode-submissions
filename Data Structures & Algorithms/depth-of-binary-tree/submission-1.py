# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result = []
        if root is None:
            return 0
        
        stack = []
        # Initialize the stack with the root and a starting depth of 1 in a list
        stack.append([root, 1]) 
        res = 0
        
        while stack:
            # Unpack the list into your 'top' node and the current depth
            top, depth = stack.pop()
            
            if top:
                result.append(top.val)
                
                # Logic to calculate Max depth
                res = max(res, depth)
                
                # Append the child node along with the incremented depth
                if top.left:
                    stack.append([top.left, depth + 1])
                if top.right:   
                    stack.append([top.right, depth + 1])
                    
        return res