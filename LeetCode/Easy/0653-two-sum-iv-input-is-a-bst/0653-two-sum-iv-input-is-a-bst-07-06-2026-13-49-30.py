# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root, isReverse):
        self.__stack = []
        self.reverse = isReverse
        self.pushAll(root)
    
    def pushAll(self, root):
        while root:
            self.__stack.append(root)
            if self.reverse:
                root = root.right
            else: 
                root = root.left

    def hasNext(self):
        if not self.__stack:
            return False
        return True

    def next(self):
        tmpNode = self.__stack.pop()
        if not self.reverse:
            self.pushAll(tmpNode.right)
        else:
            self.pushAll(tmpNode.left)

        return tmpNode.val

class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: 2* O(h)
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        
        l = BSTIterator(root, False)
        r = BSTIterator(root, True)

        i = l.next()
        j = r.next()

        while i < j:
            if i+j == k:
                return True
            elif i+j < k:
                i = l.next()
            else:
                j = r.next()
        return False