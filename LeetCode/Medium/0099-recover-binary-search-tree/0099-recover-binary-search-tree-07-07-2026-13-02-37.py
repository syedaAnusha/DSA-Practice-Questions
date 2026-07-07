# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Brute Force Approach
    # Time Complexity: O(n) + O(nlogn) + O(n)
    # Space Complexity: O(n) + O(n)
    def inorder(self, root, inorderList):
        cur = root
        while cur:
            if not cur.left:
                inorderList.append(cur.val)
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                if not prev.right:
                    prev.right = cur
                    inorderList.append(cur.val)
                    cur = cur.left
                else:
                    prev.right = None
                    cur = cur.right
        inorderList.sort()

    def correctBST(self, root, inList):
        if not root:
            return
        
        self.correctBST(root.left, inList)
        root.val = inList[self.index]
        self.index += 1
        self.correctBST(root.right, inList)

        return root

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        inorderlist = []
        self.index = 0
        self.inorder(root, inorderlist)
        self.correctBST(root, inorderlist)