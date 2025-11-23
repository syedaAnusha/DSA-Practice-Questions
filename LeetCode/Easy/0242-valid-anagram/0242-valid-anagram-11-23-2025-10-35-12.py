class Solution:
    # Brute Force Approach
    # Time Complexity: O(n)
    # Space Complexity: O(n) since, they store exact same characters
    def isAnagram(self, s: str, t: str) -> bool:
        m1 = {};
        m2 = {};
        if len(s) != len(t):
            return False;
            
        for i in range(len(s)):
            if s[i] in m1:
                m1[s[i]] += 1;
            else:
                m1[s[i]] =  1;
            if t[i] in m2:
                m2[t[i]] += 1;
            else:
                m2[t[i]] = 1;
        
        if m1 != m2:
            return False;
        return True;
        