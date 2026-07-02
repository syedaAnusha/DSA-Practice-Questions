# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

# return the Kth largest element in the given BST rooted at 'root'
class Solution:
    # Optimal Approach
    # Time Complexity: O(n) + O(n)
    # Space Complexity: O(1)
    def findNumOfNodes(self, root):
        numOfNodes = 0
        st = [root]
        while st:
            node = st.pop()
            numOfNodes += 1
            if node.left:
                st.append(node.left)
            if node.right:
                st.append(node.right)
        return numOfNodes
        
    def kthLargest(self,root, k):
        #your code here
        if not root:
            return 
        totalNodes = self.findNumOfNodes(root)
        cnt = 0
        cur = root
        kthIndex = totalNodes - k
        
        while cur:
            if not cur.left:
                if cnt == kthIndex:
                    return cur.data
                cnt += 1
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
                    if cnt == kthIndex:
                        return cur.data
                    cnt += 1
                    cur = cur.right
        
        