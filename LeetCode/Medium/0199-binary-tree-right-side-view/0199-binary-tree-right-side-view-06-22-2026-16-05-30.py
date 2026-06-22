from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Optimal Approach - Using Recursion
    # Time Complexity: O(n)
    # Space Complexity: O(n) for skewed tree in worst case and O(h) in an avg and best case   
    def findAllRightSideViewNodes(self, root, level, arr):
        if not root:
            return
        if level == len(arr):
            arr.append(root.val)
        self.findAllRightSideViewNodes(root.right, level+1, arr)
        self.findAllRightSideViewNodes(root.left, level+1, arr)
        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        self.findAllRightSideViewNodes(root, 0, ans)
        return ans