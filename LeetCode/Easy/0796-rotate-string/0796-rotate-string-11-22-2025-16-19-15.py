class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s);
        g = len(goal);

        if n != g:
            return False;

        for i in range(n):
            char = s[0];
            tempStr = s[1:];
            tempStr = tempStr + char;
            s =  tempStr;
            if s == goal:
                return True;
        return False;


        