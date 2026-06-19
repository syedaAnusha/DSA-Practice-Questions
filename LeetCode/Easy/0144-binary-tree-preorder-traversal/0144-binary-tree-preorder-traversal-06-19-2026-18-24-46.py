# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative Approach
    # Time Complexity: O(2n)
    # Space Complexity: O(n) +  O(n)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        tempStack = [root]
        while tempStack:
            curRoot = tempStack.pop()
            ans.append(curRoot.val)
            if curRoot.right:
                tempStack.append(curRoot.right)
            if curRoot.left:
                tempStack.append(curRoot.left)
        return ans