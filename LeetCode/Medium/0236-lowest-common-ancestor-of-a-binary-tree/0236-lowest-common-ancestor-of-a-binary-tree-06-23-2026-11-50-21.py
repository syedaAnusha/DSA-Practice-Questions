# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Brute Force Approach
    # Time Complexity: O(n) + O(n) + O(n)
    # Space Complexity: O(n) + O(n)
    def findPathToNode(self, root, target, arr):
        if not root:
            return False

        arr.append(root.val)
        if root.val == target:
            return True

        if (self.findPathToNode(root.left, target, arr) or self.findPathToNode(root.right, target, arr)):
            return True

        arr.pop()
        return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pathToNodeP = []
        pathToNodeQ = []
        self.findPathToNode(root, p.val, pathToNodeP)
        self.findPathToNode(root, q.val, pathToNodeQ)
        pLen = len(pathToNodeP)
        qLen = len(pathToNodeQ)
        minLen = min(pLen, qLen)
        depeestMatch = None
        for i in range(minLen):
            if pathToNodeP[i] == pathToNodeQ[i]:
                depeestMatch = TreeNode(pathToNodeP[i])
            else:
                break  
        return depeestMatch
        