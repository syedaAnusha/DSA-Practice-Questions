# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        cur = root
        nodeVal = float('-inf')
        while cur:
            if not cur.left:
                if nodeVal >= cur.val:
                    return False
                nodeVal = cur.val 
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                if not prev.right:
                    prev.right = cur
                    cur = cur.left
                else:
                    prev.right = None
                    if nodeVal >= cur.val:
                        return False
                    nodeVal = cur.val
                    cur = cur.right
        return True        