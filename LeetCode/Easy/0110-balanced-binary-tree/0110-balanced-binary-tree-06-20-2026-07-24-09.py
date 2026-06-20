# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Brute Force Approach
    # Time Complexity: O(n) * O(n)
    # Space Complexity: O(n)
    def findHeight(self, root):
        if not root:
            return 0
        else:
            lh = self.findHeight(root.left)
            rh = self.findHeight(root.right)
            maxHeight = 1 + max(lh, rh)
        return maxHeight

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        leftH = self.findHeight(root.left)
        rightH = self.findHeight(root.right)

        if abs(leftH - rightH) > 1:
            return False

        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)

        if not right or not left:
            return False

        return True   