# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(h)
    def findNumOfNodes(self, root, cntNodes):
        if not root or (not root.left and not root.right):
            return

        if root.left:
            cntNodes[0] += 1 
        self.findNumOfNodes(root.left,  cntNodes)
        if root.right:
            cntNodes[0] += 1 
        self.findNumOfNodes(root.right, cntNodes)

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        cntNodes = [1]
        self.findNumOfNodes(root, cntNodes)
        return cntNodes[0]   