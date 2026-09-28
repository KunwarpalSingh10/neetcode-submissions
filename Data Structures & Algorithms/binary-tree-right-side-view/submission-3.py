# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Time Complexity: O(n), where n is the number of nodes
        Space Complexity: O(n), where n is the number of nodes
        """
        q = collections.deque()
        q.append(root)
        res = []

        while q:
            rightmost = None
            length = len(q)
            for _ in range(length):
                node = q.popleft()
                if node:
                    rightmost = node.val
                    q.append(node.left)
                    q.append(node.right)
            if rightmost:
                res.append(rightmost)
        return res