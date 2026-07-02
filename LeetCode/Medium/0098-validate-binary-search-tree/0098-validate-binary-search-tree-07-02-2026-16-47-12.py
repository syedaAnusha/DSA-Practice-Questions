# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Optimal Approach - 02
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def checkValidBST(self, root, minVal, maxVal):
        if not root:
            return True
        if root.val >= maxVal or root.val <= minVal:
            return False
        return self.checkValidBST(root.left, minVal, root.val) and self.checkValidBST(root.right, root.val, maxVal)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkValidBST(root, float('-inf'), float('inf')) 