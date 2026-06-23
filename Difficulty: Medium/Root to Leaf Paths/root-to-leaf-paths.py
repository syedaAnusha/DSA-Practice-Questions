from collections import deque
"""
Definition of Node
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    # Optimal Approach
    # Time Complexity: O(n/2) + O(l*h)
    # Space Complexity: O(n) 
    def findAllPaths(self, root, paths, path):
        if not root:
            return 
        
        path.append(root.data)
        if not root.left and not root.right:
            paths.append(list(path))
            return
        else:
            if root.left:
                self.findAllPaths(root.left, paths, path)
                path.pop()
            if root.right:
                self.findAllPaths(root.right, paths, path)
                path.pop()
        
    def Paths(self, root):
        # code here
        paths, path = [], []
        self.findAllPaths(root, paths, path)
        return paths