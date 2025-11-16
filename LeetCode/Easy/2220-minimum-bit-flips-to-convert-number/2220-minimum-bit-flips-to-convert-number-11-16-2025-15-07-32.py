class Solution:
    # Optimal Approach
    # Time Complexity: O(log (start ^ goal))
    # Space Complexity: O(1)
    def getCountOfFlippedBits(self, n):
        cnt = 0;
        while n > 0:
            cnt += (n & 1);
            n = n >> 1;
        return cnt;

    def minBitFlips(self, start: int, goal: int) -> int:
        n = start ^ goal;
        return self.getCountOfFlippedBits(n);
        