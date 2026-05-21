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
        while left <= right and right < lengthOfStr:
            if s[right] not in freqMap:
                freqMap[s[right]] = right;
            elif left <= freqMap[s[right]]:
                left = freqMap[s[right]] + 1;
                freqMap[s[right]] = right;
            else:
                freqMap[s[right]] = right;
            maxLengthStr = max(maxLengthStr, right-left+1);
            right += 1;
        return maxLengthStr;