# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Better Approach
    # Time Complexity: O(n) + O(nlogn) + O(n)
    # Space Complexity: O(2n)
    def constructBST(self, preorder, preStart, preEnd, inorder, inStart, inEnd, inMpp):
        if preStart > preEnd or inStart > inEnd:
            return
        root = TreeNode(preorder[preStart])
        inRoot = inMpp[root.val]
        numsLeft = inRoot - inStart

        root.left = self.constructBST(preorder, preStart+1, preStart+numsLeft, inorder, inStart, inRoot-1,inMpp)
        root.right = self.constructBST(preorder, preStart+numsLeft+1, preEnd, inorder, inRoot+1, inEnd, inMpp)
        return root

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = sorted(preorder)
        mpp = {}
        for i in range(len(inorder)):
            mpp[inorder[i]] = i
        return self.constructBST(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1, mpp)