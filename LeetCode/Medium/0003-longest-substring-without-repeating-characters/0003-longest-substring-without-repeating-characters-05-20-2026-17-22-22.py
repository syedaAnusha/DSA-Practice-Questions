class Solution:
    # Brute Force Approach - 02
    # Time Complexity: O(n^2)
    # Space Complexity: O(n + n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        lengthOfStr = len(s);
        maxLengthStr = 0;
        for i in range(lengthOfStr):
            freqMap = {};
            for j in range(i, lengthOfStr):
                if s[j] in freqMap:
                    break;
                freqMap[s[j]] = 1;
                maxLengthStr = max(maxLengthStr, j-i+1);
        return maxLengthStr;    