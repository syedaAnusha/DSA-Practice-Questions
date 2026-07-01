"""
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    # Optimal Approach
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def minValue(self, root):
        # code here
        if not root:
            return -1
        minValue = float('inf')
        while root and root.data < minValue:
            minValue = min(minValue, root.data)
            root = root.left
        return minValue
            
        