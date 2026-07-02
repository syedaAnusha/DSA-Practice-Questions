# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Optimal Approach Using Morris traversal
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def findKthNode(self, root, k):
        cnt = 0
        while root:
            if not root.left:
                cnt += 1
                if cnt == k:
                    return root.val
                root = root.right
            else:
                prev = root.left
                while prev.right and prev.right != root:
                    prev = prev.right
                if not prev.right:
                    prev.right = root
                    root = root.left 
                else:
                    prev.right = None
                    cnt += 1
                    if cnt == k:
                        return root.val
                    root = root.right
            
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        return self.findKthNode(root, k)