# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Time Complexity: O(n), it goes through every node in the Tree once
        Space Complexity: O(n), it stores all the nodes from the tree in the hashmap
        """
        hashmap = {}
        self.curr = 0
        for i, val in enumerate(inorder):
            hashmap[val] = i
        
        def search(left, right):
            if left > right:
                return None
            rootVal = preorder[self.curr]
            self.curr += 1
            root = TreeNode(rootVal)
            index = hashmap[rootVal]

            root.left = search(left, index - 1)
            root.right = search(index + 1, right)

            return root
        
        return search(0, len(inorder) - 1)