'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def findPreOrder(self, root, arr):
        if root == None:
            return
        arr.append(root.data)
        self.findPreOrder(root.left, arr)
        self.findPreOrder(root.right, arr)
        
    def preOrder(self, root):
    # code here
        arr = []
        self.findPreOrder(root, arr)
        return arr
    