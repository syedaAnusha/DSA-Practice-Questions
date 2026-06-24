from collections import deque, defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Optimal Approach
    # Time Complexity: O(n) + O(n)
    # Space Complexity: O(n) + O(n) + O(n) 
    def isLeaf(self, root):
        return (not root.left and not root.right)

    def mapParents(self, root):
        mpp = {}
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
                mpp[node.left] = node
            if node.right:
                q.append(node.right)
                mpp[node.right] = node
        return mpp
    
    def findNodesWithDistanceK(self, targetNode, k, mpp):
        q = deque([targetNode])
        visited = set()
        visited.add(targetNode)
        curDistance = 0

        while q and curDistance != k:
            level_size = len(q)
            for _ in range(level_size):
                node = q.popleft()
                if node.left and node.left not in visited:
                    q.append(node.left)
                    visited.add(node.left)
                if node.right and node.right not in visited:
                    q.append(node.right)
                    visited.add(node.right)
                if node in mpp and mpp[node] not in visited:
                    q.append(mpp[node])
                    visited.add(mpp[node])
            curDistance += 1
        return [node.val for node in q]
    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        mpp = self.mapParents(root)
        return self.findNodesWithDistanceK(target, k, mpp)