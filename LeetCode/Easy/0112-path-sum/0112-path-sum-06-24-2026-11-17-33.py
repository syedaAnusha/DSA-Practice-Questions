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
    def isLeaf(self, root):
        return (not root.left and not root.right)

    def checkForPathSum(self, root, target, cur):
        if not root:
            return False
        if self.isLeaf(root):
            if cur == target:
                return True
            else:
                return False
        if (root.left and self.checkForPathSum(root.left,target,cur+root.left.val)) or (root.right and self.checkForPathSum(root.right,target,cur+root.right.val)):
            return True
        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.checkForPathSum(root, targetSum, root.val)   