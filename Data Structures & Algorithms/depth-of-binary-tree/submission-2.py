# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = -1
        def dfs(node):
            if node is None:
                return 0

            left_val = dfs(node.left)
            right_val = dfs(node.right)

            max_depth = max(left_val,right_val) + 1
            return max_depth
        return dfs(root)

