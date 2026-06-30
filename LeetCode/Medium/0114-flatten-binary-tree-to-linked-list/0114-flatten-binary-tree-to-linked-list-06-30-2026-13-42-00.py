# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Optimal - Morris Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        node = root
        while node:
            if node.left:
                prev = node.left
                while prev.right:
                    prev = prev.right
                prev.right = node.right
                node.right = node.left
                node.left = None
            node = node.right