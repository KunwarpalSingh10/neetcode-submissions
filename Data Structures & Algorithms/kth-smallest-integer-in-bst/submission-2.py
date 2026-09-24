# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root, arr):
            if not root:
                return

            if root:
                arr.append(root.val)

            dfs(root.left,arr)
            dfs(root.right,arr)

            return arr
        
        return sorted(dfs(root,[]))[k - 1]