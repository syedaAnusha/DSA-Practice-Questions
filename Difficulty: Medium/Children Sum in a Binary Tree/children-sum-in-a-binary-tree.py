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
    # Optimal Approach Using level order traversal
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def isLeaf(self, root):
        return (not root.left and not root.right)
        
    def isSumProperty(self, root):
        # code here
        if self.isLeaf(root):
            return True
        q = deque([root])
        
        while q:
            Sum = 0
            node = q.popleft()
            if not self.isLeaf(node):
                if node.left:
                    Sum += node.left.data
                    q.append(node.left)
                if node.right:
                    Sum += node.right.data
                    q.append(node.right)
                if Sum != node.data:
                    return False
        return True