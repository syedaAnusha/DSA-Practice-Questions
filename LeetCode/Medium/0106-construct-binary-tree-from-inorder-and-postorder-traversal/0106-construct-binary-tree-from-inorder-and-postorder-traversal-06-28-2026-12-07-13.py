# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def constructBinaryTree(self, postorder, postStrt, postEnd, inorder, inStrt, inEnd, inMpp):
        if inStrt > inEnd or postEnd > postStrt:
            return
        root = TreeNode(postorder[postStrt])
        inRoot = inMpp[root.val]
        numsLeft = inEnd - inRoot

        root.left = self.constructBinaryTree(postorder,postStrt-numsLeft-1,postEnd,inorder,inStrt,inRoot-1,inMpp)
        root.right = self.constructBinaryTree(postorder,postStrt-1,postStrt-numsLeft,inorder,inRoot+1,inEnd,inMpp)
        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        
        inMpp = {}
        for i in range(len(inorder)):
            inMpp[inorder[i]] = i
        
        root = self.constructBinaryTree(postorder, len(postorder)-1, 0, inorder, 0, len(inorder)-1, inMpp)
        return root 