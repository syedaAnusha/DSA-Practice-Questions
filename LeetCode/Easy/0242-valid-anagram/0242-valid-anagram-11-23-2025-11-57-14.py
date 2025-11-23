class Solution:
    # Optimal Approach - for all unicode characters
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        frequencyMap = {};
        if len(s) != len(t):
            return False;

        for char in s:
            if char in frequencyMap:
                frequencyMap[char] += 1;
            else:
                frequencyMap[char] = 1;
        for char in t:
            if char not in frequencyMap:
                return False;
            frequencyMap[char] -= 1;
            if frequencyMap[char] == 0:
                del frequencyMap[char];
        return len(frequencyMap) == 0;