# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Optimal Approach - 02
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def inorder(self, root): 
        cur = root
        while cur:
            if not cur.left:
                self.checkBstForCorrectOrder(cur)
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                if not prev.right:
                    prev.right = cur
                    cur = cur.left     
                else:
                    prev.right = None
                    self.checkBstForCorrectOrder(cur)
                    cur = cur.right

    def checkBstForCorrectOrder(self, node):
        if self.prevNode and node.val < self.prevNode.val:
            if not self.firstNode:
                self.firstNode = self.prevNode
                self.middleNode = node
            else:
                self.lastNode = node
        else:
            self.prevNode = node

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