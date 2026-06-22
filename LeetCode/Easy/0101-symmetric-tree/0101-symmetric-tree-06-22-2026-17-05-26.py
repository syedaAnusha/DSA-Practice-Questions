# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def findSymmetry(self, left, right):
        if not left or not right:
            return (left == right)
        if left.val != right.val:
            return False
        return (self.findSymmetry(left.left, right.right) and self.findSymmetry(left.right, right.left))
       
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.findSymmetry(root.left, root.right)