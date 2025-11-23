class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def isAnagram(self, s: str, t: str) -> bool:
        frequencyArr = [0 for _ in range(26)];
        if len(s) != len(t):
            return False;

        for i in range(len(s)):
            index = ord(s[i]) - ord('a');
            frequencyArr[index] += 1;
        
        for j in range(len(t)):
            index = ord(t[j]) - ord('a'); 
            frequencyArr[index] -= 1;

        for k in range(26):
            if frequencyArr[k] != 0:
                return False;
        return True;
