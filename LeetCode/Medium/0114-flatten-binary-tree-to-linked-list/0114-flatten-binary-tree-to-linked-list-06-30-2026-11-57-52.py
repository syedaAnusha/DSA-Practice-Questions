# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Brute Force Approach
    # Time Complexity: O(2n) + O(n) = O(n)
    # Space Complexity: O(2n) = O(n)
    def preorder(self, root):
        pre = []
        st = [root]
        while st:
            node = st.pop()
            pre.append(node.val)
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
        return pre

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