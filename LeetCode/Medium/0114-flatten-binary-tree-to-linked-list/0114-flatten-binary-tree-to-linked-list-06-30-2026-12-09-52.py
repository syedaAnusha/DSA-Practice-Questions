# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Better Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def preorder(self, root):
        preorder = []
        cur = root
        while cur:
            if not cur.left:
                preorder.append(cur.val)
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                if not prev.right:
                    prev.right = cur
                    preorder.append(cur.val)
                    cur = cur.left
                else:
                    prev.right = None
                    cur = cur.right
        return preorder

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        nodesVal = self.preorder(root)
        node = root
        for i in range(1,len(nodesVal)):
            if node.left:
                node.left = None
            node.right = TreeNode(nodesVal[i])
            node = node.right
        return root