from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def findLevelOrderTraversal(self, root):
        if not root:
            return []
        ans = []
        q = deque([root])
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level)
        return ans   
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = self.findLevelOrderTraversal(root)
        return ans