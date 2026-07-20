# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Better Approach
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def isLeaf(self, node):
        return (not node.left and not node.right)

    def preorder(self, root):
        if not root:
            return 0
        if self.isLeaf(root):
            self.countDominantNodes += 1
            return root.val

        left = self.preorder(root.left)
        right = self.preorder(root.right)
        maxNode = max(left, right)
        if root.val >= maxNode:
            self.countDominantNodes += 1
            return root.val
        return maxNode
        
    def countDominantNodes(self, root: TreeNode | None) -> int:
        self.countDominantNodes = 0
        if not root:
            return self.countDominantNodes
        if self.isLeaf(root):
            self.countDominantNodes += 1
            return self.countDominantNodes
        self.preorder(root)
        return self.countDominantNodes