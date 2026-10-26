# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        queue = deque([root])

        while queue:
            level = len(queue)

            for i in range(level):
                node = queue.popleft()
                
                # THE LOGIC: If this is the LAST node in the current level loop,
                # it means it is the right-most node. Add it to our view!
                if i == level - 1:
                    result.append(node.val)
                
                # 4. Queue up the next level (Always Left, then Right)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result