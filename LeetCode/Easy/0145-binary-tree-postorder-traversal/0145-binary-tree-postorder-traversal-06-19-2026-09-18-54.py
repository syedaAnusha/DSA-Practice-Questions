# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative Approach using 1 stack
    # Time Complexity: O(2n)
    # Space Complexity: O(2n)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                temp = stack[-1].right
                if not temp:
                    temp = stack.pop()
                    ans.append(temp.val)
                    while stack and temp == stack[-1].right:
                        temp = stack.pop()
                        ans.append(temp.val)
                else:
                    node = temp
        return ans