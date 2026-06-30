# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Brute Force Approach - using recursion
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    prevNode = None
    def flattenHelper(self, node):
        if not node:
            return
        self.flattenHelper(node.right)
        self.flattenHelper(node.left)
        node.right = self.prevNode
        node.left = None
        self.prevNode = node  

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flattenHelper(root)           