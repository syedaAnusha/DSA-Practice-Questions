# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Better Approach using stack
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        st = [root]
        while st:
            node = st.pop()
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
            if st:
                node.right = st[-1]
            node.left = None