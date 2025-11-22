class Solution:
    # Brute Force Approach
    # Time Complexity: O(n + k log n) or k = n then O(n + n log n)
    # Space Complexity: O(n) + O(2k) or k = n then O(n)
    def frequencySort(self, s: str) -> str:
        hashMap = dict();
        ans = "";
        for i in range(len(s)-1,-1,-1):
            if s[i] in hashMap:
                hashMap[s[i]] += 1;
            else:
                hashMap[s[i]] = 1;
        sorted_map = dict(sorted(hashMap.items(), key=lambda item: item[1], reverse=True))
        for key, value in sorted_map.items():
            tempStr = key*value;
            ans += tempStr # every character stored only once!

        return ans;