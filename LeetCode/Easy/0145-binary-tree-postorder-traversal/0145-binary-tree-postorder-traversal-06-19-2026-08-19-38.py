# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative Approach using 2 stacks
    # Time Complexity: O(2n)
    # Space Complexity: O(2n)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        node = root
        if not node:
            return []
        stack1 = [node]
        stack2 = []
        while stack1:
            node = stack1.pop()
            stack2.append(node.val)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)        
        return stack2[::-1]