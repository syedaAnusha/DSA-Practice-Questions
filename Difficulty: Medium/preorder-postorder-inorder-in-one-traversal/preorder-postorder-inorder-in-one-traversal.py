# Time Complexity: O(3n)
# Space Complexity: O(4n)
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class Solution:
    def findAllInOneTraversal(self, root):
        preorder , inorder , postorder = [], [], []
        if not root:
            return []
        
        stack = [(root, 1)]
        while stack:
            node, num = stack.pop()
            if num == 1:
                preorder.append(node.val)
                stack.append((node, 2))
                if node.left:
                    stack.append((node.left, 1))
            
            elif num == 2:
                inorder.append(node.val)
                stack.append((node, 3))
                if node.right:
                    stack.append((node.right, 1))

            else:
                postorder.append(node.val)
        
        return [preorder, inorder, postorder]
        

if __name__ == "__main__":
    root = TreeNode(1)
    # left subtree
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    # right subtree
    root.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    sol = Solution()
    traversals = sol.findAllInOneTraversal(root)
    preorder, inorder, postorder = traversals[0], traversals[1], traversals[2]
    print("Preorder Traversal:", *preorder)
    print("Preorder Traversal:", *inorder)
    print("Preorder Traversal:", *postorder)
