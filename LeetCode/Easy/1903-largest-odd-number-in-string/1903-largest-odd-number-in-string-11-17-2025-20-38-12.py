class Solution:
    # Better Approach
    # Time Complexity: O(n);
    # Space Complexity: O(1)
    def largestOddNumber(self, num: str) -> str:
        maxOddInt = "";
        n = len(num)-1;

        # check if last digit is odd e.g. 1,3,5,7,9
        lastDigit = int(num[n]);
        if lastDigit & 1 == 1:
            return num;
        
        # check if largest odd number is in between even
        while n >= 0:
            if int(num[n]) & 1 == 1:
                return num[:n+1];
            n -= 1;

        return maxOddInt;