class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(); # remove leading whitespaces
        i = 0;
        sign = 1;
        parsedInt = 0;
        INT_MIN = -2147483648;
        INT_MAX = 2147483647;

        if len(s) == 0:
            return parsedInt; 

        if s[i] == '+':
            i += 1;
        elif s[i] == '-':
            i += 1;
            sign = -1;
        
        while i < len(s):
            if not s[i].isdigit():
                break;
            else:
                parsedInt = parsedInt * 10 + int(s[i]);
            i += 1;

        parsedInt *= sign;

        if parsedInt < INT_MIN:
            return INT_MIN;
        elif parsedInt > INT_MAX:
            return INT_MAX;
        else:
            return parsedInt;
