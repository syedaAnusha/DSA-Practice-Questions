class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(256)
    def longestKSubstr(self, s, k):
        # code here
        hashMap = {};
        left = right= 0;
        maxLen = 0;
        lenOfStr = len(s);
        
        while right < lenOfStr:
            if s[right] in hashMap:
                hashMap[s[right]] += 1;
            else:
                hashMap[s[right]] = 1;
            if len(hashMap) == k:
                maxLen = max(maxLen, right-left+1);
                
            if len(hashMap) > k:
                hashMap[s[left]] -= 1;
                if hashMap[s[left]] == 0:
                    hashMap.pop(s[left]);
                left += 1;
            right += 1;
        
        if maxLen == 0:
            return -1;
        return maxLen;