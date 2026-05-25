class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(26) // k only contains english upper case letters
    def characterReplacement(self, s: str, k: int) -> int:
        totalLenOfStr = len(s);
        maxLen = 0;
        left = right = 0;
        hashMap = {};
        maxFreq = 0;
        while right < totalLenOfStr:
            if s[right] in hashMap:
                hashMap[s[right]] += 1;
            else:
                hashMap[s[right]] = 1;
            maxFreq = max(maxFreq, hashMap[s[right]]);
            curLen = right - left + 1;
            positionToChange =  curLen - maxFreq;
            if positionToChange > k:
                hashMap[s[left]] -= 1;
                left += 1;
                curLen = right - left + 1;
                maxFreq = 0;
            maxLen = max(maxLen, curLen);
            right += 1;
        return maxLen;