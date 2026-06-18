# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def findPostorderTraversal(self, root, arr):
        if root == None:
            return
        self.findPostorderTraversal(root.left, arr)
        self.findPostorderTraversal(root.right, arr)
        arr.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.findPostorderTraversal(root, arr)
        return arr    