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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            leftHeight = self.maxDepth(root.left)
            rightHeight = self.maxDepth(root.right)
            maxHeight = 1 + max(leftHeight, rightHeight)
        return maxHeight     