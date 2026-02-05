class Solution:
    # Brute Approach - using recursion
    # Time Complexity: O(2^n)
    # Space Complexity: O(n)
    def generateAllBinStrs(self, result, subStr, n):
        if len(subStr) == n:
            result.append(subStr);
            return result;
        
        self.generateAllBinStrs(result, subStr+"0", n);
        
        if not subStr or subStr[-1] != 1:
            self.generateAllBinStrs(result, subStr+"1", n);
                
    def binstr(self, n):
        # code here
       result = [];
       self.generateAllBinStrs(result, "", n);
       return result;