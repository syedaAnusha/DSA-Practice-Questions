from collections import deque
'''
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    # Optimal Approach
    # Time Complexity: O(n) + O(n)
    # Space Complexity: O(n) + O(n) + O(n) = O(n)
    def makeParentsAndFindTargetNode(self, root, target, mpp):
        q = deque([root])
        targetNode = None
        while q:
            node = q.popleft()
            if node.data == target:
                targetNode = node
            if node.left:
                mpp[node.left] = node
                q.append(node.left)
            if node.right:
                mpp[node.right] = node
                q.append(node.right)
        return targetNode
        
                
    def minTime(self, root, target):
        # code here
        if not root:
            return 0
        mpp = {}
        targetNode = self.makeParentsAndFindTargetNode(root, target, mpp)
        q = deque([targetNode])
        burnedNodes = set()
        burnedNodes.add(targetNode)
        minTime = 0
        
        while q:
            N = len(q)
            flagBurned = False
            for _ in range(N):
                node = q.popleft()
                if node.left and node.left not in burnedNodes:
                    flagBurned = True
                    q.append(node.left)
                    burnedNodes.add(node.left)
                if node.right and node.right not in burnedNodes:
                    flagBurned = True
                    q.append(node.right)
                    burnedNodes.add(node.right)
                if node in mpp and mpp[node] not in burnedNodes:
                    flagBurned = True
                    q.append(mpp[node])
                    burnedNodes.add(mpp[node])
            if flagBurned:
                minTime += 1
            
        return minTime
