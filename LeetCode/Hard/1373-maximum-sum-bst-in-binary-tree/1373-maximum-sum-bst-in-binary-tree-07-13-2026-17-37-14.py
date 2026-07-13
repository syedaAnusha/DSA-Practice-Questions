# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class NodeValue:
    def __init__(self, minNode, maxNode, Sum):
        self.minNode = minNode
        self.maxNode = maxNode
        self.Sum = Sum

class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    INT_MIN = float('-inf')
    INT_MAX = float('inf')
    maxSum = 0

    def maxSumSubtreeHelper(self, root):
        if not root:
            return NodeValue(self.INT_MAX, self.INT_MIN, 0)
        
        left = self.maxSumSubtreeHelper(root.left)
        right = self.maxSumSubtreeHelper(root.right)

        if left.maxNode < root.val and root.val < right.minNode:
            curSum = left.Sum + right.Sum + root.val
            self.maxSum = max(self.maxSum, curSum)

            return NodeValue(
                min(left.minNode, root.val), 
                max(right.maxNode, root.val), 
                curSum,
            )
        
        return NodeValue(
                self.INT_MIN,
                self.INT_MAX,
                max(left.Sum, right.Sum),
            )
        
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.maxSumSubtreeHelper(root)
        return self.maxSum