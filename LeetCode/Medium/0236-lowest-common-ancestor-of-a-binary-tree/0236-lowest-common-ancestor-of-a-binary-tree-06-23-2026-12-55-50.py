# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def findLCA(self, root, valP, valQ):
        if not root or root.val == valP or root.val == valQ:
            return root
        
        left = self.findLCA(root.left, valP, valQ)
        right = self.findLCA(root.right, valP, valQ)

        if not left:
            return right
        elif not right:
            return left
        else:
            return root

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.findLCA(root, p.val, q.val)
