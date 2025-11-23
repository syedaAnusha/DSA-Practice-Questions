class Solution:
    # Optimal Approach
    # Time Compexity: O(n)
    # Space Complexity: O(1)
    def removeOuterParentheses(self, s: str) -> str:
        ans = "";
        i = 0;
        openBracCount = 0;
        closeBracCount = 0;
        start = 0;
        n = len(s);
        while i < n:
            if s[i] == '(':
                openBracCount += 1;
            if s[i] == ')':
                closeBracCount += 1;
            if openBracCount == closeBracCount:
                ans += s[start+1:i];
                openBracCount = 0;
                closeBracCount = 0;
                start = i+1;

            i += 1;
        return ans;

