# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative Approach
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        tempStack = []
        ans = []
        node = root
        while True:
            if node:
                tempStack.append(node)
                node = node.left
            else:
                if not tempStack:
                    break
                node = tempStack.pop()
                ans.append(node.val)
                node = node.right
        return ans