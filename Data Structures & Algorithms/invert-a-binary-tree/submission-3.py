# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            # 1. Base Case: Reached a leaf's child
            if not node:
                return None 
                
            # 2. Pre-order logic (Top-Down): 
            # (Nothing needed here for the bottom-up approach)
            
            # 3. Recursive calls: 
            # Go all the way down and get the fully inverted left and right subtrees
            left_val = dfs(node.left)
            right_val = dfs(node.right)
            
            # 4. Post-order logic (Bottom-Up): 
            # Take the fully inverted subtrees and assign them to the opposite sides
            node.left = right_val
            node.right = left_val
            
            # 5. Return data to the parent
            return node 

        # Trigger the recursive function and return the final inverted root
        return dfs(root)