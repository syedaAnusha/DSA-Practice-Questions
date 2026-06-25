# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Optimal Approach - 02
    # Time Complexity: O(log n) * O(log n)
    # Space Complexity: O(h)
    def findLeftHeight(self, root):
        height = 0
        while root:
            height += 1
            root = root.left
        return height
    
    def findRightHeight(self, root):
        height = 0
        while root:
            height += 1
            root = root.right
        return height
         
    def findNumOfNodes(self, root):
        if not root:
            return 0
        lh = self.findLeftHeight(root)
        rh = self.findRightHeight(root)
        if lh == rh:
            return ((1<<lh) - 1)

        return 1 + self.findNumOfNodes(root.left) + self.findNumOfNodes(root.right)  

    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.findNumOfNodes(root)