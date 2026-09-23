# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val != subRoot.val:
                return False
            
            left, right = isSameTree(root.left,subRoot.left), isSameTree(root.right, subRoot.right)

            return left and right

        def dfs(node):
            if not node:
                return False
            
            if isSameTree(node, subRoot):
                return True
            
            left, right = dfs(node.left), dfs(node.right)

            return left or right
        
        return dfs(root)

            




