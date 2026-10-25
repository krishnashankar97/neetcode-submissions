# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result = []
        if not root:
            return result
        queue = deque([root])
        

        while queue:
            level_size = len(queue)
            current_level = []
            
            # Process every node in this level
            for _ in range(level_size):
                head = queue.popleft()
                current_level.append(head.val)

                if head.left:
                    queue.append(head.left)
                if head.right:
                    queue.append(head.right)
                    
            # Append the fully built level to the final result
            result.append(current_level)
        
        return result