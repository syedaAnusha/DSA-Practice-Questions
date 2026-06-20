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
    def findHeight(self, root):
        if not root:
            return 0
        else:
            lh = self.findHeight(root.left)
            if lh == -1:
                return -1
            rh = self.findHeight(root.right)
            if rh == -1:
                return -1
            if (abs(lh-rh) > 1):
                return -1;
            maxHeight = 1 + max(lh, rh)
        return maxHeight

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return (self.findHeight(root) != -1)  