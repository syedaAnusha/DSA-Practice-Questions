from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Optimal Approach
    # Time Complexity: O(n/2) + O(n/2)
    # Space Complexity: O(n/2) + O(n/2)
    def findAllRightSideViewNodes(self, root):
        mpp = {}
        stack = [(root, 0)]
        while stack:
            N = len(stack)
            for _ in range(N):
                node, row = stack.pop()
                if row not in mpp:
                    mpp[row] = node.val
                if node.left:
                    stack.append((node.left, row+1))
                if node.right:
                    stack.append((node.right, row+1))
        return mpp
                
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        nodes = self.findAllRightSideViewNodes(root)
        for val in nodes.values():
            ans.append(val)
        return ans 