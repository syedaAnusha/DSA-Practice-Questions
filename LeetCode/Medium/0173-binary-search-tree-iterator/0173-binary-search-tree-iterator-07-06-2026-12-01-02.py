# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    # Optimal Approach
    # Time Complexity: O(1) on average
    # Space Complexity: O(h)
    def pushAll(self, root, stack):
        while root:
            stack.append(root)
            root = root.left

    def __init__(self, root: Optional[TreeNode]):
        self.__stack = [] 
        self.pushAll(root, self.__stack)

    def next(self) -> int:
        node = self.__stack.pop()
        self.pushAll(node.right, self.__stack)
        return node.val

    def hasNext(self) -> bool:
        if not self.__stack:
            return False
        return True
        
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()