class Solution:
    # Brute Force Approach
    # Time Complexity: O(3^n)
    # Space Complexity O(n)
    # Note: Better approach will be using DP which takes T.C as O(n^2) and S.C as O(n^2)
    def checkForValidString(self, s, index, cnt):
        if cnt < 0:
            return False
        if index >= len(s):
            return (cnt == 0)
        if s[index] == '(':
            return self.checkForValidString(s, index+1, cnt+1)
        elif s[index] == ')':
            return self.checkForValidString(s, index+1, cnt-1)
        
        return (self.checkForValidString(s, index+1, cnt-1) or self.checkForValidString(s, index+1, cnt+1) or self.checkForValidString(s, index+1, cnt))
            
    def checkValidString(self, s: str) -> bool:
        return self.checkForValidString(s, 0, 0)     
