''' 
class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None 
'''

class Solution:
    # Optimal Approach - Using Recursion
    # Time Complexity: O(n)
    # Space Complexity: O(n) for skewed tree in worst case and O(h) in an avg and best case  
    def findAllLeftSideViewNodes(self, root, level, arr):
        if not root:
            return
        if level == len(arr):
            arr.append(root.data)
        self.findAllLeftSideViewNodes(root.left, level+1, arr)
        self.findAllLeftSideViewNodes(root.right, level+1, arr)
        
    def leftView(self, root):
        # code here
        ans = []
        if not root:
            return ans
        self.findAllLeftSideViewNodes(root, 0, ans)
        return ans
        