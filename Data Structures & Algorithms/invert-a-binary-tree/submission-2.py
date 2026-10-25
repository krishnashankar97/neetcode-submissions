# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return root

        result = []
        queue = deque()
        queue.append(root)

        while queue:
            head = queue.popleft()
            if head:
                result.append(head.val)
            # Swap left and right node in the tree
                head.left, head.right = head.right, head.left
                if head.left:
                    queue.append(head.left)
                if head.right:
                    queue.append(head.right)

        return root