# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    # Brute Force Approach
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    
    def inOrder(self, root, inorderlist):
        cur =  root
        while cur:
            if not cur.left:
                inorderlist.append(cur.val)
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
                    inorderlist.append(cur.val)
                    cur = cur.right

    def __init__(self, root: Optional[TreeNode]):
        self.inorderList = [] 
        self.inOrder(root, self.inorderList)
        self.iterator = -1


    def next(self) -> int:
        self.iterator += 1
        return self.inorderList[self.iterator]

    def hasNext(self) -> bool:
        if self.iterator >= len(self.inorderList)-1:
            return False
        return True
        
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()