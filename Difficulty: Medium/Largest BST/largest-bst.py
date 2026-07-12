''' Structure of a Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class NodeValue:
    def __init__(self, minNode, maxNode, maxSize):
        self.minNode = minNode
        self.maxNode = maxNode
        self.maxSize = maxSize
        
class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    INT_MIN = float('-inf')
    INT_MAX = float('inf')
    
    def largestBSTSubTreeHelper(self, root):
        if not root:
            return NodeValue(self.INT_MAX, self.INT_MIN, 0)
        
        left = self.largestBSTSubTreeHelper(root.left)
        right = self.largestBSTSubTreeHelper(root.right)
        
        if left.maxNode < root.data and root.data < right.minNode:
            return NodeValue(
                min(root.data, left.minNode), 
                max(root.data, right.maxNode), 
                left.maxSize + right.maxSize + 1
            )
        
        return NodeValue(
            self.INT_MIN, 
            self.INT_MAX, 
            max(left.maxSize, right.maxSize)
        )
        
    def largestBst(self, root):
        # Your code here
        return self.largestBSTSubTreeHelper(root).maxSize