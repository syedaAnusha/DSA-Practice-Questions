from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def serializeHelp(self, root):
        q = deque([root])
        res = ""
        while q:
            node = q.popleft()
            if node is None:
                res += "#,"
            else:
                res += str(node.val) + ","
                q.append(node.left)
                q.append(node.right)

        return res

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode 
        :rtype: str
        """
        if not root:
            return ""
        return self.serializeHelp(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nodes = data.split(',')
        index = 1
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        while q and index < len(nodes)-1:
            node = q.popleft()
            if nodes[index] != '#':
                left = TreeNode(int(nodes[index]))
                node.left = left
                q.append(left)
            index+=1

            if nodes[index] != '#':
                right = TreeNode(int(nodes[index]))
                node.right = right
                q.append(right)
            index +=1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))