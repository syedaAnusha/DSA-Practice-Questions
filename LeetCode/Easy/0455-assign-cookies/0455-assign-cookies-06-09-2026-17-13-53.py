import heapq;
class Solution:
    # Brute Force Approach
    # Time Complexity: O(s+g log s+g) O(min(s, g))
    # Space Complexity: O(1)
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i, G = 0, len(g);
        j, S = 0, len(s);
        s.sort();
        g.sort();
        maxNumberOfChildren = 0;
        if not s:
            return 0;
        while i < G and j < S:
            if s[j] >= g[i]:
                maxNumberOfChildren += 1;
                i += 1;
            j += 1;
        return maxNumberOfChildren;      