# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Optimal Approach
    # Time Complexity: O(2n)
    # Space Complexity: O(p+q)
    def preOrderTraversal(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return (self.preOrderTraversal(p.left, q.left) and self.preOrderTraversal(p.right, q.right))
        else:
            return False
        return True 

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.preOrderTraversal(p,q)
        