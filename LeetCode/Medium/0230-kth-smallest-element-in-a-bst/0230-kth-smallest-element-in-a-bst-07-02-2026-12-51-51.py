# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Better Approach Using Inorder traversal
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def findAllNodes(self, root):
        st = []
        ans = []
        while True:
            if root:
                st.append(root)
                root = root.left
            else:
                if not st:
                    break
                node = st.pop()
                ans.append(node.val)
                root = node.right
        return ans
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = self.findAllNodes(root)
        return nodes[k-1]       