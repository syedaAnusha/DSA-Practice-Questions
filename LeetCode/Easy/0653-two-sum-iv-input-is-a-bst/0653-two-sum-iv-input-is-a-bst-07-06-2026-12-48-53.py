# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Brute Force Approach
    # Time Complexity: O(n) + O(n/2)
    # Space Complexity: O(n)
    def inOrderTraversal(self, root, st):
        cur = root
        while cur:
            if not cur.left:
                st.append(cur.val)
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
                    st.append(cur.val)
                    cur = cur.right

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        stack = []
        self.inOrderTraversal(root, stack)
        i = 0
        j = len(stack)-1
        while i < j:
            if stack[i]+stack[j] == k:
                return True
            elif stack[i]+stack[j] < k:
                i += 1
            else:
                j -= 1
        return False       