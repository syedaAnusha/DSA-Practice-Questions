class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def romanToInt(self, s: str) -> int:
        romanToIntMap = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000};
        intValue = 0;
        i = 0;

        while i < len(s)-1:
            curNum = romanToIntMap[s[i]];
            nextNum = romanToIntMap[s[i+1]];

            if curNum < nextNum:
                newNum = nextNum - curNum;
                intValue += newNum;
                i += 2;
            else:
                intValue += curNum;
                i += 1;

        if i != len(s):
            intValue += romanToIntMap[s[-1]];
        return intValue;
        





        
        