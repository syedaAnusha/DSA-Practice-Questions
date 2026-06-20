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
    maxDiameter = 0
    def findHeight(self, root):
        if not root:
            return 0
        
        lh = self.findHeight(root.left)
        rh = self.findHeight(root.right)
        self.maxDiameter = max(self.maxDiameter, lh + rh)
        return 1 + max(lh, rh)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.findHeight(root)
        return self.maxDiameter