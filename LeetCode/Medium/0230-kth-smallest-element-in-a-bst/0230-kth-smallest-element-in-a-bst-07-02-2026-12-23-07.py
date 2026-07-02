# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Brute Force Approach
    # Time Complexity: O(n) + O(n log n)
    # Space Complexity: O(n)
    def findAllNodes(self, root):
        st = [root]
        ans = []
        while st:
            node = st.pop()
            ans.append(node.val)
            if node.right:
                st.append(node.right)
            if node.left: 
                st.append(node.left)
        return ans
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = self.findAllNodes(root)
        nodes.sort()
        return nodes[k-1]       