# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def findPreOrder(self, root, arr):
        if root == None:
            return
        arr.append(root.val)
        self.findPreOrder(root.left, arr)
        self.findPreOrder(root.right, arr)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.findPreOrder(root, arr)
        return arr    