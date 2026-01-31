class Solution:
    # Optimal Approach using recursion
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Aux Space Complexity: O(n) for recursion calls
    def convertToInteger(self, s, index, parsedInt):
        if index == len(s) or not s[index].isdigit():
            return parsedInt;
        parsedInt = parsedInt * 10 + int(s[index]);
        return self.convertToInteger(s, index+1, parsedInt); 
        
    def myAtoi(self, s: str) -> int:
        textWithoutWhiteSpaces = s.lstrip();
        print()
        if len(textWithoutWhiteSpaces) == 0:
            return 0;
        INT_MIN = -2147483648;
        INT_MAX = 2147483647;
        sign = 1;
        index = 0;
        if  textWithoutWhiteSpaces[index] == '-':
            sign = -1;
            index += 1;
        elif textWithoutWhiteSpaces[index] == '+':
            index += 1;
        
        parsedInt = self.convertToInteger(textWithoutWhiteSpaces, index, 0);
        parsedInt *= sign;
        if parsedInt < INT_MIN:
            return INT_MIN;
        elif parsedInt > INT_MAX:
            return INT_MAX;
        else:
            return parsedInt;       