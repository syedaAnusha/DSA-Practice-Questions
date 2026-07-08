# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Optimal Approach - 01
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def inorder(self, root):  
        if not root:
            return

        self.inorder(root.left)
        if self.prevNode  and root.val < self.prevNode.val:
            if not self.firstNode:
                self.firstNode = self.prevNode
                self.middleNode = root
            else:
                self.lastNode = root
        self.prevNode = root
        self.inorder(root.right)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.firstNode = None
        self.prevNode = TreeNode(float('-inf'))
        self.middleNode = None
        self.lastNode = None
        self.inorder(root)
        if self.firstNode and self.lastNode:
            self.firstNode.val, self.lastNode.val = self.lastNode.val, self.firstNode.val
        elif self.firstNode and self.middleNode:
            self.firstNode.val, self.middleNode.val = self.middleNode.val, self.firstNode.val