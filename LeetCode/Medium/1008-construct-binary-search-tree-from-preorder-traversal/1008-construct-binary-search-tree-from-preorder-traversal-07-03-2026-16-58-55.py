# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Optimal Approach
    # Time Complexity: O(3n) = O(n)
    # Space Complexity: O(n)
    def constructBST(self, preorder, maxVal):
        if self.index == len(preorder) or preorder[self.index] > maxVal:
            return
        root = TreeNode(preorder[self.index])
        self.index += 1
        root.left = self.constructBST(preorder, root.val)
        root.right = self.constructBST(preorder, maxVal)
        return root
        
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.index = 0
        return self.constructBST(preorder, float('inf'))