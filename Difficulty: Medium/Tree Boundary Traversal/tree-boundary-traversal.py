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
    # Time Complexity: O(3n)
    # Space Complexity: O(n)
    def isLeaf(self, root):
        return (not root.left and not root.right)
            
    def addLeftBoundary(self, root, arr):
        node = root.left
        while node:
            if not self.isLeaf(node):
                arr.append(node.data)
            if node.left:
                node = node.left
            else:
                node = node.right
    
    def addAllLeafNodes(self, root, arr):
        if self.isLeaf(root):
            arr.append(root.data)
            return
        if root.left:
            self.addAllLeafNodes(root.left, arr)
        if root.right:
            self.addAllLeafNodes(root.right, arr)
        
    def addRightBoundary(self, root, arr):
        node = root.right
        temp = []
        while node:
            if not self.isLeaf(node):
                temp.append(node.data)
            if node.right:
                node = node.right
            else:
                node = node.left
        for i in range(len(temp)-1, -1, -1):
            arr.append(temp[i])
        
    def boundaryTraversal(self, root):
        # code here
        res = []
        if not root:
            return res
        
        if not self.isLeaf(root):
            res.append(root.data)
        
        self.addLeftBoundary(root, res)
        self.addAllLeafNodes(root, res)
        self.addRightBoundary(root, res)
        return res
            
            