from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([(root,0)])
        maxWidth = 0
        while q:
            firstIndex = 0
            lastIndex = 0
            minIndex = q[0][1] 
            size = len(q)
            for i in range(size):
                node, index = q.popleft()
                curIndex = index - minIndex
                if i == 0:
                    firstIndex = index
                if i == size-1:
                    lastIndex = index

                if node.left:
                    pair = (node.left, (2*curIndex)+1)
                    q.append(pair)

                if node.right:
                    pair = (node.right, (2*curIndex)+2)
                    q.append(pair)

            maxWidth = max(maxWidth, lastIndex-firstIndex+1)             
        return maxWidth