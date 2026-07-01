'''
Definition for Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 
'''
        
class Solution:
    # Optimal Approach 
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def findCeil(self,root, x):
        # code here
        ans = -1
        while root:
            rootVal = root.data
            if rootVal >= x:
                ans = rootVal
                root = root.left
            else:
                root = root.right
        return ans