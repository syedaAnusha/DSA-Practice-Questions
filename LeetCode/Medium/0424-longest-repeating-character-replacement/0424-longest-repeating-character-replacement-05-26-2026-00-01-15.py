class Solution:
    # Better Approach
    # Time Complexity: O(n+n) * O(26)
    # Space Complexity: O(26) // k only contains english upper case letters
    def findMaxFreq(self, hashMap):
        maxChar = 0;
        for key, value in hashMap.items():
            maxChar = max(maxChar, value);
        return maxChar;

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
            while positionToChange > k:
                hashMap[s[left]] -= 1;
                left += 1;
                maxFreq = 0;
                maxFreq = max(maxFreq, self.findMaxFreq(hashMap));
                curLen = right - left + 1;
                positionToChange =  curLen - maxFreq;
            maxLen = max(maxLen, curLen);
            right += 1;
        return maxLen;