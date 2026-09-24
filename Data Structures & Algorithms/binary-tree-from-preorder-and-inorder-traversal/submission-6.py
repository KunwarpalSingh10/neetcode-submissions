# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # prestart is where there the root is currently at
        # instart is the boundary for inorder from left of prestart
        # inend is the bounary for inorder from right of prestart
        # inindex represents where the root is located within the inorder
        hashmap = {}
        for i in range(len(inorder)):
            hashmap[inorder[i]] = i

        def helper(prestart, instart, inend, preorder, inorder):
            if prestart > len(preorder) - 1 or instart > inend:
                return None
            root = TreeNode(preorder[prestart])
            
            inindex = hashmap[root.val]
            root.left = helper(prestart + 1, instart, inindex - 1, preorder, inorder)
            root.right = helper(prestart + (inindex - instart) + 1, inindex + 1, inend, preorder, inorder)

            return root

        return helper(0, 0, len(inorder) - 1, preorder, inorder)