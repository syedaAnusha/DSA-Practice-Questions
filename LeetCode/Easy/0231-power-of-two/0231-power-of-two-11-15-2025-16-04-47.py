class Solution:
    # Optimal Approach
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def isPowerOfTwo(self, n: int) -> bool:
        if n != 0:
            if n & (n-1) == 0:
                return True;
        return False;