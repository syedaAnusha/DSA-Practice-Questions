# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Morris Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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