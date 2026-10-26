# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            
            left_val = dfs(root.left)
            right_val = dfs(root.right)

            res = max(res, left_val + right_val)

            return 1+max(left_val,right_val)
        dfs(root)
        return res