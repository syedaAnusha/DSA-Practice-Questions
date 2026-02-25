class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def isValid(self, s: str) -> bool:
        stack = [];
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i]);
            else:
                if len(stack) == 0:
                    return False;
                curVal = stack.pop();
                if s[i] == ')' and curVal == '(' or s[i] == ']' and curVal == '[' or s[i] == '}' and curVal == '{':
                    continue;
                else:
                    return False; 
        if len(stack) > 0:
            return False;
        return True;     