''' Structure of a Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    # Brute Force Approach
    # Time Complexity: O(n)*O(n)
    # Space Complexity: O(n)
    def validateBST(self, root):
        cur = root
        nodeVal = float('-inf')
        while cur:
            if not cur.left:
                if nodeVal >= cur.data:
                    return False
                nodeVal = cur.data
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                if not prev.right:
                    prev.right = cur
                    cur = cur.left
                else:
                    prev.right = None
                    if nodeVal >= cur.data:
                        return False
                    nodeVal = cur.data
                    cur = cur.right
        return True
    
    def findNumOfNodes(self, root):
        st = [root]
        cnt = 0
        while st:
            node = st.pop()
            cnt += 1
            
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
        return cnt

                
    def largestBst(self, root):
        # Your code here
        if not root:
            return 0
            
        maxSize = 0
        st = [root]
        
        while st:
            node = st.pop()
            if self.validateBST(node):
                maxSize = max(maxSize, self.findNumOfNodes(node))
            
            if node.right:
                st.append(node.right)
                
            if node.left:
                st.append(node.left)
                
        return maxSize
