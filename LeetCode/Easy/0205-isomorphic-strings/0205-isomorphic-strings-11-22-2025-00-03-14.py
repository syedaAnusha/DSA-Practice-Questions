class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def isIsomorphic(self, s: str, t: str) -> bool:
        i = 0;
        m1 = {};
        m2 = {};

        while i < len(s):
            if s[i] not in m1:
                m1[s[i]] = i;
            if t[i] not in m2:
                m2[t[i]] = i;

            # check if both indexes are same
            if m1[s[i]] != m2[t[i]]:
                return False;
            i += 1;
        return True;
        