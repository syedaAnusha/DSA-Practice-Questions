'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    # Optimal Approach
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def findMaxFork(self, root, k):
        #code here
        floor = -1
        while root:
            val = root.data
            if val <= k:
                floor = val
                root = root.right
            else:
                root = root.left
        return floor