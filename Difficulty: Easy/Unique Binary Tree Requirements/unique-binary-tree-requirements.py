class Solution:
    # Optimal Approach
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def isPossible(self, a, b):
        #Code here
        # 2 = Inorder Traversal
        if a == 2 and b == 2:
            return False
        if a == 2 or b == 2:
            return True
        else:
            return False