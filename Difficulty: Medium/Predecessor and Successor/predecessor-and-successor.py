'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    # optimal Approach
    # Time Complexity: O(h)
    # Space Complexity: O(n)
    def helperPreSuc(self, root, key):
        if not root:
            return 
        if root.data > key and root.data < self.successor.data:
            self.successor = root
            self.helperPreSuc(root.left, key)
        elif root.data < key and root.data > self.predecessor.data:
            self.predecessor = root
            self.helperPreSuc(root.right, key)
        else:
            self.helperPreSuc(root.left, key)
            self.helperPreSuc(root.right, key)
            
    def findPreSuc(self, root, key):
        # code here
        self.predecessor = Node(float('-inf'))
        self.successor = Node(float('inf'))
        if not root:
            return
        self.helperPreSuc(root, key)
        if self.predecessor.data == float('-inf'):
            self.predecessor = None
        if self.successor.data == float('inf'):
            self.successor = None
        return [self.predecessor, self.successor]