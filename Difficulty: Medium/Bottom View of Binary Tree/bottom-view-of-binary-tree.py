from collections import deque
'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    # Optimal Approach
    # Time Complexity: O(n) + O(nlogn)
    # Space Complexity: O(n/2) + O(n/2)
    
    def findAllBottomViewNodes(self, root):
        q = deque([(root, 0)])
        mpp = {}
        while q:
            N = len(q)
            for _ in range(N):
                node, col = q.popleft()
                if col not in mpp:
                    mpp[col] = node.data
                else:
                    mpp[col] = node.data
                if node.left:
                    q.append((node.left, col-1))
                if node.right:
                    q.append((node.right, col+1))
        return mpp
        
    def bottomView(self, root):
        # code here
        ans = []
        if not root:
            return ans
        nodes = self.findAllBottomViewNodes(root)
        for col in sorted(nodes.keys()):
            ans.append(nodes[col])
        return ans
        