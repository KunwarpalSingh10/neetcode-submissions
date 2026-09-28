# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Time Complexity: O(n), where n is the number of nodes
        Space Complexity: O(h), where h is the height of the tree
        """

        self.res = 0

        def dfs(node, maxi):
            if not node:
                return
            
            if node.val >= maxi:
                self.res += 1
                maxi = node.val
            
            dfs(node.left, maxi)
            dfs(node.right, maxi)

            return node

        dfs(root, root.val)
        return self.res

