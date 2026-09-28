# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Time Complexity: O(n), going to each node and measuring its depth
        Space Complexity: O(h), as we measure depth level by level
        """
        self.total = 0

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            self.total = max(self.total, left + right)
            return 1 + max(left, right)

        dfs(root)
        return self.total
