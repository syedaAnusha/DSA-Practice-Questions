class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity O(1)        
    def checkValidString(self, s: str) -> bool:
        minVal = 0
        maxVal = 0
        for i in range(len(s)):
            if s[i] == "(":
                minVal += 1
                maxVal += 1
            elif s[i] == ")":
                minVal -= 1
                maxVal -= 1
            else:
                minVal -= 1
                maxVal += 1
            if minVal < 0:
                minVal = 0
            if maxVal < 0:
                return False
        return (minVal == 0)     