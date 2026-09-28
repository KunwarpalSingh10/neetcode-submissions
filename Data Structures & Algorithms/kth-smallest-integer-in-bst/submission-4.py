# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def find(node):
            if not node:
                return
            
            res.append(node.val)

            find(node.left)
            find(node.right)

            return node
        find(root)
        return sorted(res)[k - 1]