class Solution:
    # Optimal Approach - 2
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxDepth(self, s: str) -> int:
        counter = 0;
        maxNestedDepth = float('-inf');
        for i in range(len(s)):
            if s[i] == '(':
                counter += 1;
            elif s[i] == ')':
                counter -= 1;

            maxNestedDepth = max(maxNestedDepth, counter);
        return maxNestedDepth;


            

        