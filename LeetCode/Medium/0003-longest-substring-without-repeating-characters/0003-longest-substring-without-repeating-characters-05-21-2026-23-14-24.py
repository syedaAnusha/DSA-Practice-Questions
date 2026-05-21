class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(256)
    def lengthOfLongestSubstring(self, s: str) -> int:
        lengthOfStr = len(s);
        maxLengthStr = 0;
        freqMap = {};
        left = 0;
        right = 0;
        while right < lengthOfStr:
            if s[right] in freqMap:
                if left <= freqMap[s[right]]:
                    left = freqMap[s[right]] + 1;
            maxLengthStr = max(maxLengthStr, right-left+1);
            freqMap[s[right]] = right;
            right += 1;
        return maxLengthStr;