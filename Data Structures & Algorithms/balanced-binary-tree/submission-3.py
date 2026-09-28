# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Time Complexity: O(n), we are visiting all nodes
        Space Complexity: O(h), we are processing height by height with stack
        """
        self.check = 0
        
        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            if abs(left - right) > 1:
                self.check += 1
            
            return 1 + max(left, right)

        dfs(root)

        return self.check == 0
                