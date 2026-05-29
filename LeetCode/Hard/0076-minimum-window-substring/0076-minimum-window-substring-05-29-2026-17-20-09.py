class Solution:
    # Optimal Approach
    # Time Complexity: O(n) + O(m)
    # Space Complexity: O(m)
    def storeTcharsInHashMap(self, t):
        hashMap = {};
        for Str in t:
            if Str in hashMap:
                hashMap[Str] += 1;
            else:
                hashMap[Str] = 1;
        return hashMap;

    def minWindow(self, s: str, t: str) -> str:
        minLen = float("inf");
        startIndex = endIndex = -1;
        left = right = 0;
        cnt = 0;
        hashMap = self.storeTcharsInHashMap(t);

        while right < len(s):
            if s[right] in hashMap:
                if hashMap[s[right]] > 0:
                    cnt += 1;
                hashMap[s[right]] -= 1;
            while left < len(s) and cnt == len(t):
                if right-left+1 < minLen:
                    minLen = min(minLen, right-left+1);
                    startIndex = left;
                    endIndex = startIndex + minLen;
                
                if s[left] in hashMap:
                    if hashMap[s[left]] <= 0:
                        hashMap[s[left]] += 1;
                    if hashMap[s[left]] > 0:
                        cnt -= 1;
                left += 1;

            right += 1;

 
        if startIndex == -1:
            return "";
        return s[startIndex:endIndex];      