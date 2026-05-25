class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(3)
    def numberOfSubstrings(self, s: str) -> int:
        substrCount = 0;
        totalSLen = len(s);
        left = right = 0;
        hashMap = {'a': 0, 'b': 0, 'c': 0};

        while right < totalSLen:
            hashMap[s[right]] += 1;
            while hashMap['a'] > 0 and hashMap['b'] > 0 and hashMap['c'] > 0:
                substrCount += totalSLen - right;
                hashMap[s[left]] -= 1;
                left += 1;
            right += 1;
        return substrCount;