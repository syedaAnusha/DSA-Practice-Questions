# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Aux Space Complexity: O(n)
    def constructBT(self, preorder, preStrt, preEnd, inorder, inStrt, inEnd, inMpp):
        if preStrt > preEnd or inStrt > inEnd:
            return
        root = TreeNode(preorder[preStrt])
        inRoot = inMpp[root.val]
        numsLeft = inRoot - inStrt

        root.left = self.constructBT(preorder, preStrt+1, preStrt+numsLeft, inorder, inStrt, inRoot-1, inMpp)
        root.right = self.constructBT(preorder, preStrt+numsLeft+1, preEnd, inorder, inRoot+1, inEnd, inMpp)

        return root
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        inorderMpp = {}
        for i in range(len(inorder)):
            inorderMpp[inorder[i]] = i
        root = self.constructBT(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1, inorderMpp)
        return root  