from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Better Approach
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        leftToRight = True
        queue = deque([root])
        while queue:
            N = len(queue)
            level = [0]*N
            for i in range(N):
                node = queue.popleft()
                if leftToRight:
                    index = i
                else:
                    index = N - 1 - i
                level[index] = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)   
            ans.append(level)
            leftToRight = not leftToRight
            
        return ans       