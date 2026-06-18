# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def findInorderTraversal(self, root, arr):
        if root == None:
            return

        self.findInorderTraversal(root.left, arr)
        arr.append(root.val)
        self.findInorderTraversal(root.right, arr)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.findInorderTraversal(root, arr)
        return arr      