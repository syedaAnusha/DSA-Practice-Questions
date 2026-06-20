# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(n) when skewed binary Tree , O(log n) when complete binary tree 
    def findMaxPathSum(self, root, maxValue):
        if not root:
            return 0

        left = max(0, self.findMaxPathSum(root.left, maxValue))
        right = max(0, self.findMaxPathSum(root.right, maxValue))
        maxValue[0] = max(maxValue[0], left + right + root.val)
        longestPathSum = max(left, right) + root.val
        return longestPathSum

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxValue = [float('-inf')]
        self.findMaxPathSum(root, maxValue)
        return maxValue[0]   