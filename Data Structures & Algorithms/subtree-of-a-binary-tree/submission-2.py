# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checker(A, B):
            if not A and not B:
                return True
            if not A or not B:
                return False
            if A.val != B.val: 
                return False
            
            left, right = checker(A.left, B.left), checker(A.right, B.right)
            return left and right

        def find(node):
            if not node:
                return False
            if checker(node, subRoot):
                return True
            
            left, right = find(node.left), find(node.right)

            return left or right
        
        return find(root)
        