from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Optimal Approach
    # Time Complexity: O(n) + O(log N * log N)
    # Space Complexity: o(n) for deque + O(n/2) for hashmap in case if it is a balanced binary tree 
    def findAllColValues(self, root):
        q = deque([(root, 0, 0)])
        hashMap = {}
        while q:
            for _ in range(len(q)):
                node, row, col = q.popleft()
                if col not in hashMap:
                    hashMap[col] = {}
                if row not in hashMap[col]:
                    hashMap[col][row] = []
                hashMap[col][row].append(node.val)
                if node.left:
                    q.append((node.left, row+1, col-1))
                if node.right:
                    q.append((node.right, row+1, col+1))
        return hashMap
                       
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = self.findAllColValues(root)
        ans = []
        for c in sorted(nodes.keys()):
            col = []
            for r in nodes[c].keys():
                col.extend(sorted(nodes[c][r]))
            ans.append(col)
        return ans