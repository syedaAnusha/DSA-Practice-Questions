class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxDepth(self, s: str) -> int:
        openBrac = 0;
        closeBrac = 0;
        maxNestedDepth = float('-inf');
        for i in range(len(s)):
            maxNestedDepth = max(maxNestedDepth, openBrac-closeBrac);
            if s[i] == '(':
                openBrac += 1;
            elif s[i] == ')':
                closeBrac += 1;
        return maxNestedDepth;


            

        