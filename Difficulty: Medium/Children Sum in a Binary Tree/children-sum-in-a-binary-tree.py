from collections import deque
'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    # Optimal Approach Using DFS
    # Time Complexity: O(n)
    # Space Complexity: O(h)
    def isLeaf(self, root):
        return (not root.left and not root.right)
    
    def checkSumProperty(self, root):
        if not root:
            return 0
        
        if self.isLeaf(root):
            return root.data
        
        leftSum = self.checkSumProperty(root.left)
        rightSum = self.checkSumProperty(root.right)
        if root.data != (leftSum + rightSum):
            return float('-inf')
        else:
            return root.data
        
    def isSumProperty(self, root):
        # code here
        return (self.checkSumProperty(root) != float('-inf'))
        