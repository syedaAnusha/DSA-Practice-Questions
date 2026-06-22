from collections import deque
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
# Optimal Approach
# Time Complexity: O(n) + O(logn * logn)
# Space Complexity: O(n) + O(n/2)
class Solution:
    def findTopView(self, root):
        nodes = {}
        q = deque([(root, 0, 0)])
        hashMap = {}
        while q:
            N = len(q)
            for _ in range(N):
                node, row, col = q.popleft()
                if col not in hashMap:
                    hashMap[col] = {}
                    hashMap[col][row] = []
                    hashMap[col][row].append(node.data)
                if node.left:
                    q.append((node.left, row+1, col-1))
                if node.right:
                    q.append((node.right, row+1, col+1))
        return hashMap
                
    def topView(self, root):
        # code here
        ans = []
        if not root:
            return ans
            
        nodes = self.findTopView(root)
        for col in sorted(nodes.keys()):
            for row in sorted(nodes[col].keys()):
                ans.extend(nodes[col][row])
        return ans