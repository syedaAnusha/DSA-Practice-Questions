class Solution:
    # Brute Force Approach
    # Time Complexity: O(2^(2*n)*n)
    # Space Complexity: O(n)
    def isValidParenthesis(self, subStr, totalLenOfSubStr):
        openParen = 0
        i = 0;
        while i < totalLenOfSubStr:
            if openParen < 0:
                return False;
            elif subStr[i] == '(':
                openParen += 1;
            elif subStr[i] == ')' and openParen >= 0:
                openParen -= 1;
            i += 1;
        if openParen == 0:
            return True;
        return False;


    def helperGenerateParenthesis(self, subStr, result, totalLenOfSubStr):
        if len(subStr) == totalLenOfSubStr:
            if self.isValidParenthesis(subStr, totalLenOfSubStr):
                result.append(subStr);
            return result;
        self.helperGenerateParenthesis(subStr+"(", result, totalLenOfSubStr);
        self.helperGenerateParenthesis(subStr+")", result, totalLenOfSubStr);
        
    def generateParenthesis(self, n: int) -> List[str]:
        totalLenOfSubStr = 2*n
        result = [];
        self.helperGenerateParenthesis("",result,totalLenOfSubStr)
        return result;
        