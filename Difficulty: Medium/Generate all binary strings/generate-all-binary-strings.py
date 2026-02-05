class Solution:
    # Brute Approach - using recursion
    # Time Complexity: O(2^n)
    # Space Complexity: O(n)
    def generateAllBinStrs(self, result, subStr, n):
        if len(subStr) == n:
            result.append(subStr);
            return result;
            
        # First try to generate all binary strings with 0
        self.generateAllBinStrs(result, subStr+"0", n);
        # then generatr all binary strings with 1
        self.generateAllBinStrs(result, subStr+"1", n);
                
    def binstr(self, n):
        # code here
       result = [];
       self.generateAllBinStrs(result, "", n);
       return result;
